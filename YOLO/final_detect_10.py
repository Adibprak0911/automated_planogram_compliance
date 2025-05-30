import argparse
import csv
import os
import platform
import sys
from pathlib import Path


import torch
import matplotlib.pyplot as plt


FILE = Path(__file__).resolve()
ROOT = FILE.parents[0]  # YOLOv5 root directory
if str(ROOT) not in sys.path:
    sys.path.append(str(ROOT))  # add ROOT to PATH
ROOT = Path(os.path.relpath(ROOT, Path.cwd()))  # relative

from ultralytics.utils.plotting import Annotator, colors, save_one_box

from models.common import DetectMultiBackend
from utils.dataloaders import IMG_FORMATS, VID_FORMATS, LoadImages, LoadScreenshots, LoadStreams
from utils.general import (
    LOGGER,
    Profile,
    check_file,
    check_img_size,
    check_imshow,
    check_requirements,
    colorstr,
    cv2,
    increment_path,
    non_max_suppression,
    print_args,
    scale_boxes,
    strip_optimizer,
    xyxy2xywh,
)
from utils.torch_utils import select_device, smart_inference_mode


#@smart_inference_mode()
def apply_yolo(
    weights = ROOT/"runs/train/exp/weights/best.pt",
    source = ROOT/"dataset/test/updated.jpg",
    data = ROOT/"data.yaml",

    imgsz=(640, 640),  # inference size (height, width)
    conf_thres=0.25,  # confidence threshold
    iou_thres=0.45,  # NMS IOU threshold
    max_det=1000,  # maximum detections per image
    device="",  # cuda device, i.e. 0 or 0,1,2,3 or cpu
    view_img=False,  # show results
    save_txt=False, #  save results to *.txt
    save_csv=False,  # save results in CSV format
    save_conf=False,  # save confidences in --save-txt labels
    save_crop=True,  # save cropped prediction boxes
    nosave=False,  # do not save images/videos
    classes=None,  # filter by class: --class 0, or --class 0 2 3
    agnostic_nms=False,  # class-agnostic NMS
    augment=False,  # augmented inference
    visualize=False,  # visualize features
    update=False,  # update all models
    project= "MASTER/yolo_results",  # save results to project/name
    name="exp",  # save results to project/name
    exist_ok=False,  # existing project/name ok, do not increment
    line_thickness=3,  # bounding box thickness (pixels)
    hide_labels=False,  # hide labels
    hide_conf=False,  # hide confidences
    half=False,  # use FP16 half-precision inference
    dnn=False,  # use OpenCV DNN for ONNX inference
    vid_stride=1,  # video frame-rate stride
):
    source = str(source)
    save_img = not nosave and not source.endswith(".txt")  # save inference images
    is_file = Path(source).suffix[1:] in (IMG_FORMATS + VID_FORMATS)
    is_url = source.lower().startswith(("rtsp://", "rtmp://", "http://", "https://"))
    webcam = source.isnumeric() or source.endswith(".streams") or (is_url and not is_file)
    screenshot = source.lower().startswith("screen")
    if is_url and is_file:
        source = check_file(source)  # download

    # Directories
    # save_dir = increment_path(Path(project) / name, exist_ok=exist_ok)  # increment run
    # (save_dir / "labels" if save_txt else save_dir).mkdir(parents=True, exist_ok=True)  # make dir
    save_dir = increment_path(Path(project) / name, exist_ok=True)  # increment run

    # Remove the existing directory if it exists
    if save_dir.exists() and save_dir.is_dir():
        import shutil
        shutil.rmtree(save_dir)  # Remove the directory and its contents

    # Create the new directory
    save_dir.mkdir(parents=True, exist_ok=True)

    (save_dir / "labels" if save_txt else save_dir).mkdir(parents=True, exist_ok=True)  # make dir


    # Load model
    device = select_device(device)
    model = DetectMultiBackend(weights, device=device, dnn=dnn, data=data, fp16=half)
    stride, names, pt = model.stride, model.names, model.pt
    imgsz = check_img_size(imgsz, s=stride)  # check image size

    # Dataloader
    bs = 1  # batch_size
    if webcam:
        view_img = check_imshow(warn=True)
        dataset = LoadStreams(source, img_size=imgsz, stride=stride, auto=pt, vid_stride=vid_stride)
        bs = len(dataset)
    elif screenshot:
        dataset = LoadScreenshots(source, img_size=imgsz, stride=stride, auto=pt)
    else:
        dataset = LoadImages(source, img_size=imgsz, stride=stride, auto=pt, vid_stride=vid_stride)
    vid_path, vid_writer = [None] * bs, [None] * bs

    # Run inference
    model.warmup(imgsz=(1 if pt or model.triton else bs, 3, *imgsz))  # warmup
    seen, windows, dt = 0, [], (Profile(device=device), Profile(device=device), Profile(device=device))

    # Initialize a list to store coordinates
    coordinates_list = []

    for path, im, im0s, vid_cap, s in dataset:
        with dt[0]:
            im = torch.from_numpy(im).to(model.device)
            im = im.half() if model.fp16 else im.float()  # uint8 to fp16/32
            im /= 255  # 0 - 255 to 0.0 - 1.0
            if len(im.shape) == 3:
                im = im[None]  # expand for batch dim
            if model.xml and im.shape[0] > 1:
                ims = torch.chunk(im, im.shape[0], 0)

        # Inference
        with dt[1]:
            visualize = increment_path(save_dir / Path(path).stem, mkdir=True) if visualize else False
            if model.xml and im.shape[0] > 1:
                pred = None
                for image in ims:
                    if pred is None:
                        pred = model(image, augment=augment, visualize=visualize).unsqueeze(0)
                    else:
                        pred = torch.cat((pred, model(image, augment=augment, visualize=visualize).unsqueeze(0)), dim=0)
                pred = [pred, None]
            else:
                pred = model(im, augment=augment, visualize=visualize)
        # NMS
        with dt[2]:
            pred = non_max_suppression(pred, conf_thres, iou_thres, classes, agnostic_nms, max_det=max_det)

        # Second-stage classifier (optional)
        # pred = utils.general.apply_classifier(pred, classifier_model, im, im0s)

        # Define the path for the CSV file
        csv_path = save_dir / "predictions.csv"

        # Create or append to the CSV file
        def write_to_csv(image_name, prediction, confidence, coordinates):
            """Writes prediction data for an image to a CSV file, appending if the file exists."""
            data = {"Image Name": image_name, "Prediction": prediction, "Confidence": confidence, "Coordinates": coordinates}
            with open(csv_path, mode="a", newline="") as f:
                writer = csv.DictWriter(f, fieldnames=data.keys())
                if not csv_path.is_file():
                    writer.writeheader()
                writer.writerow(data)

        # Process predictions
        for i, det in enumerate(pred):  # per image
            seen += 1
            if webcam:  # batch_size >= 1
                p, im0, frame = path[i], im0s[i].copy(), dataset.count
                s += f"{i}: "
            else:
                p, im0, frame = path, im0s.copy(), getattr(dataset, "frame", 0)

            p = Path(p)  # to Path
            save_path = str(save_dir / p.name)  # im.jpg
            txt_path = str(save_dir / "labels" / p.stem) + ("" if dataset.mode == "image" else f"_{frame}")  # im.txt
            s += "%gx%g " % im.shape[2:]  # print string
            gn = torch.tensor(im0.shape)[[1, 0, 1, 0]]  # normalization gain whwh
            imc = im0.copy() if save_crop else im0  # for save_crop
            annotator = Annotator(im0, line_width=line_thickness, example=str(names))
            if len(det):
                det[:, :4] = scale_boxes(im.shape[2:], det[:, :4], im0.shape).round()  # rescale boxes to original image

                for *xyxy, conf, cls in reversed(det):
                    xyxy_list = [float(coord.item()) for coord in xyxy]
                    c = int(cls)  # integer class
                    label = names[c] if hide_conf else f"{names[c]}"
                    confidence = float(conf)
                    confidence_str = f"{confidence:.2f}"

                    # Append coordinates to the list
                    coordinates_list.append((p.name, label, confidence_str, xyxy_list))

                    final_coordinates = []
                    for i in coordinates_list:
                        coordinate = i[3]
                        x_coordinate = round((i[3][0] + i[3][2])/2)
                        y_coordinate = round((i[3][1] + i[3][3])/2)
                        final_coordinates.append((x_coordinate, y_coordinate))
                    x_coords, y_coords = zip(*final_coordinates)

                    # print(x_coords[-1], y_coords[-1])

                    if save_csv:
                        write_to_csv(p.name, label, confidence_str, xyxy_list)

                    if save_txt:  # Write to file
                        xywh = (xyxy2xywh(torch.tensor(xyxy).view(1, 4)) / gn).view(-1).tolist()  # normalized xywh
                        line = (cls, *xywh, conf) if save_conf else (cls, *xywh)  # label format
                        with open(f"{txt_path}.txt", "a") as f:
                            f.write(("%g " * len(line)).rstrip() % line + "\n")

                    if save_img or save_crop or view_img:  # Add bbox to image
                        c = int(cls)  # integer class
                        label = None if hide_labels else (names[c] if hide_conf else f"{names[c]} {conf:.2f}")
                        annotator.box_label(xyxy, label, color=colors(c, True))
                    if save_crop:
                        x_coord_str = str(int(x_coords[-1])) if final_coordinates else "0"
                        y_coord_str = str(int(y_coords[-1])) if final_coordinates else "0"
                        save_one_box(xyxy, imc, file=save_dir / "crops" / names[c] / f"{x_coord_str}_{y_coord_str}.jpg", BGR=True)

            # Stream results
            im0 = annotator.result()
            if view_img:
                if platform.system() == "Linux" and p not in windows:
                    windows.append(p)
                    cv2.namedWindow(str(p), cv2.WINDOW_NORMAL | cv2.WINDOW_KEEPRATIO)  # allow window resize (Linux)
                    cv2.resizeWindow(str(p), im0.shape[1], im0.shape[0])
                cv2.imshow(str(p), im0)
                cv2.waitKey(1)  # 1 millisecond

            # Save results (image with detections)
            if save_img:
                if dataset.mode == "image":
                    cv2.imwrite(save_path, im0)
                else:  # 'video' or 'stream'
                    if vid_path[i] != save_path:  # new video
                        vid_path[i] = save_path
                        if isinstance(vid_writer[i], cv2.VideoWriter):
                            vid_writer[i].release()  # release previous video writer
                        if vid_cap:  # video
                            fps = vid_cap.get(cv2.CAP_PROP_FPS)
                            w = int(vid_cap.get(cv2.CAP_PROP_FRAME_WIDTH))
                            h = int(vid_cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
                        else:  # stream
                            fps, w, h = 30, im0.shape[1], im0.shape[0]
                        save_path = str(Path(save_path).with_suffix(".mp4"))  # force *.mp4 suffix on results videos
                        vid_writer[i] = cv2.VideoWriter(save_path, cv2.VideoWriter_fourcc(*"mp4v"), fps, (w, h))
                    vid_writer[i].write(im0)

        # Print time (inference-only)
        LOGGER.info(f"{s}{'' if len(det) else '(no detections), '}{dt[1].dt * 1E3:.1f}ms")

    # Print results
    t = tuple(x.t / seen * 1e3 for x in dt)  # speeds per image
    LOGGER.info(f"Speed: %.1fms pre-process, %.1fms inference, %.1fms NMS per image at shape {(1, 3, *imgsz)}" % t)
    if save_txt or save_img:
        s = f"\n{len(list(save_dir.glob('labels/*.txt')))} labels saved to {save_dir / 'labels'}" if save_txt else ""
        LOGGER.info(f"Results saved to {colorstr('bold', save_dir)}{s}")
    if update:
        strip_optimizer(weights[0])  # update model (to fix SourceChangeWarning)
    
    # Return the coordinates list
    # return coordinates_list
    final_coordinates = []
    for i in coordinates_list:
        coordinate = i[3]
        x_coordinate = round((i[3][0] + i[3][2])/2)
        y_coordinate = round((i[3][1] + i[3][3])/2)
        final_coordinates.append((x_coordinate, y_coordinate))
    x_coords, y_coords = zip(*final_coordinates)


    # # Create the plot
    # plt.figure(figsize=(8, 6))
    # plt.scatter(x_coords, y_coords, color='blue', label='Detected Objects')

    # # Add labels and title
    # plt.xlabel('X Coordinates')
    # plt.ylabel('Y Coordinates')
    # plt.title('Object Detection Coordinates')
    # plt.legend()

    # # Display the plot
    # plt.grid(True)
    # plt.show()

    # print("Coordinates:", final_coordinates)


    # Extract x and y coordinates
    x_coords, y_coords = zip(*final_coordinates)

    # Define grid boundaries and spacing
    min_x = min(x_coords)
    max_x = max(x_coords)
    min_y = min(y_coords)
    max_y = max(y_coords)

    # Define number of grid columns and rows
    num_columns = 4  # Adjust this as needed
    num_rows = 2     # Adjust this as needed

    # Define the spacing for grid cells
    x_step = (max_x - min_x) / (num_columns - 1)
    y_step = (max_y - min_y) / (num_rows - 1)

    # Calculate labels for each point
    labels = {}
    for (x, y) in final_coordinates:
        # Determine grid position
        col = int(round((x - min_x) / x_step))
        row = int(round((y - min_y) / y_step))
        
        # Ensure labels fit within the expected range
        col = min(max(col, 0), num_columns - 1)
        row = min(max(row, 0), num_rows - 1)
        
        # Create label
        labels[(x, y)] = f"{row:02d}{col:02d}"

    # print("labels = ", labels)
    # Create the plot
    plt.switch_backend('TkAgg')
    plt.figure(figsize=(10, 8))
    plt.scatter(x_coords, y_coords, color='blue', label='Detected Objects')

    # Add labels and title
    plt.xlabel('X Coordinates')
    plt.ylabel('Y Coordinates')
    plt.title('Object Detection Coordinates')
    plt.legend()

    # Set grid limits to start from 0
    plt.xlim(0, max(x_coords) + 100)  # Add some margin to the right
    plt.ylim(0, max(y_coords) + 100)  # Add some margin to the top

    # Add grid
    plt.grid(True)

    #invert y-axis
    plt.gca().invert_yaxis()
    # Annotate each point with its label based on labels dictionary
    for (x, y) in final_coordinates:
        label = labels.get((x, y), '')
        
        plt.annotate(label, (x, y), textcoords="offset points", xytext=(0, 10), ha='center')

    # Display the plot
    plt.show()
    


    #change file names

    def rename_file(old_name, new_name):
        try:
            os.rename(old_name, new_name)
            print(f"File '{old_name}' successfully renamed to '{new_name}'.")
        except FileNotFoundError:
            print(f"File '{old_name}' not found.")
        except FileExistsError:
            print(f"File '{new_name}' already exists.")

    folder_path = project + "/exp/crops/chips"

    if not os.path.isdir(folder_path):
        print(f"folder not found: {folder_path}")
        return
    
    else:
        for filename in os.listdir(folder_path):
            if filename.endswith(".jpg"):  # Ensure we process only JPEG files
                base_name = os.path.splitext(filename)[0]  # Get filename without extension
                x, y = base_name.split('_')  # Split based on underscore
                print(x," ",y)
            value = labels[(int(x), int(y))]
            print(value)
            rename_file(folder_path + "/" + filename, folder_path + "/" + value + ".jpg")
                
            
    



    # return final_coordinates

apply_yolo()
# Get coordinates
# final_coordinates = apply_yolo()

