// generated from rosidl_generator_c/resource/idl__functions.c.em
// with input from px4:msg/VehicleRoi.idl
// generated code does not contain a copyright notice
#include "px4/msg/detail/vehicle_roi__functions.h"

#include <assert.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

#include "rcutils/allocator.h"


bool
px4__msg__VehicleRoi__init(px4__msg__VehicleRoi * msg)
{
  if (!msg) {
    return false;
  }
  // timestamp
  // mode
  // lat
  // lon
  // alt
  // roll_offset
  // pitch_offset
  // yaw_offset
  return true;
}

void
px4__msg__VehicleRoi__fini(px4__msg__VehicleRoi * msg)
{
  if (!msg) {
    return;
  }
  // timestamp
  // mode
  // lat
  // lon
  // alt
  // roll_offset
  // pitch_offset
  // yaw_offset
}

bool
px4__msg__VehicleRoi__are_equal(const px4__msg__VehicleRoi * lhs, const px4__msg__VehicleRoi * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  // timestamp
  if (lhs->timestamp != rhs->timestamp) {
    return false;
  }
  // mode
  if (lhs->mode != rhs->mode) {
    return false;
  }
  // lat
  if (lhs->lat != rhs->lat) {
    return false;
  }
  // lon
  if (lhs->lon != rhs->lon) {
    return false;
  }
  // alt
  if (lhs->alt != rhs->alt) {
    return false;
  }
  // roll_offset
  if (lhs->roll_offset != rhs->roll_offset) {
    return false;
  }
  // pitch_offset
  if (lhs->pitch_offset != rhs->pitch_offset) {
    return false;
  }
  // yaw_offset
  if (lhs->yaw_offset != rhs->yaw_offset) {
    return false;
  }
  return true;
}

bool
px4__msg__VehicleRoi__copy(
  const px4__msg__VehicleRoi * input,
  px4__msg__VehicleRoi * output)
{
  if (!input || !output) {
    return false;
  }
  // timestamp
  output->timestamp = input->timestamp;
  // mode
  output->mode = input->mode;
  // lat
  output->lat = input->lat;
  // lon
  output->lon = input->lon;
  // alt
  output->alt = input->alt;
  // roll_offset
  output->roll_offset = input->roll_offset;
  // pitch_offset
  output->pitch_offset = input->pitch_offset;
  // yaw_offset
  output->yaw_offset = input->yaw_offset;
  return true;
}

px4__msg__VehicleRoi *
px4__msg__VehicleRoi__create()
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  px4__msg__VehicleRoi * msg = (px4__msg__VehicleRoi *)allocator.allocate(sizeof(px4__msg__VehicleRoi), allocator.state);
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(px4__msg__VehicleRoi));
  bool success = px4__msg__VehicleRoi__init(msg);
  if (!success) {
    allocator.deallocate(msg, allocator.state);
    return NULL;
  }
  return msg;
}

void
px4__msg__VehicleRoi__destroy(px4__msg__VehicleRoi * msg)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (msg) {
    px4__msg__VehicleRoi__fini(msg);
  }
  allocator.deallocate(msg, allocator.state);
}


bool
px4__msg__VehicleRoi__Sequence__init(px4__msg__VehicleRoi__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  px4__msg__VehicleRoi * data = NULL;

  if (size) {
    data = (px4__msg__VehicleRoi *)allocator.zero_allocate(size, sizeof(px4__msg__VehicleRoi), allocator.state);
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = px4__msg__VehicleRoi__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        px4__msg__VehicleRoi__fini(&data[i - 1]);
      }
      allocator.deallocate(data, allocator.state);
      return false;
    }
  }
  array->data = data;
  array->size = size;
  array->capacity = size;
  return true;
}

void
px4__msg__VehicleRoi__Sequence__fini(px4__msg__VehicleRoi__Sequence * array)
{
  if (!array) {
    return;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();

  if (array->data) {
    // ensure that data and capacity values are consistent
    assert(array->capacity > 0);
    // finalize all array elements
    for (size_t i = 0; i < array->capacity; ++i) {
      px4__msg__VehicleRoi__fini(&array->data[i]);
    }
    allocator.deallocate(array->data, allocator.state);
    array->data = NULL;
    array->size = 0;
    array->capacity = 0;
  } else {
    // ensure that data, size, and capacity values are consistent
    assert(0 == array->size);
    assert(0 == array->capacity);
  }
}

px4__msg__VehicleRoi__Sequence *
px4__msg__VehicleRoi__Sequence__create(size_t size)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  px4__msg__VehicleRoi__Sequence * array = (px4__msg__VehicleRoi__Sequence *)allocator.allocate(sizeof(px4__msg__VehicleRoi__Sequence), allocator.state);
  if (!array) {
    return NULL;
  }
  bool success = px4__msg__VehicleRoi__Sequence__init(array, size);
  if (!success) {
    allocator.deallocate(array, allocator.state);
    return NULL;
  }
  return array;
}

void
px4__msg__VehicleRoi__Sequence__destroy(px4__msg__VehicleRoi__Sequence * array)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (array) {
    px4__msg__VehicleRoi__Sequence__fini(array);
  }
  allocator.deallocate(array, allocator.state);
}

bool
px4__msg__VehicleRoi__Sequence__are_equal(const px4__msg__VehicleRoi__Sequence * lhs, const px4__msg__VehicleRoi__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!px4__msg__VehicleRoi__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
px4__msg__VehicleRoi__Sequence__copy(
  const px4__msg__VehicleRoi__Sequence * input,
  px4__msg__VehicleRoi__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    const size_t allocation_size =
      input->size * sizeof(px4__msg__VehicleRoi);
    rcutils_allocator_t allocator = rcutils_get_default_allocator();
    px4__msg__VehicleRoi * data =
      (px4__msg__VehicleRoi *)allocator.reallocate(
      output->data, allocation_size, allocator.state);
    if (!data) {
      return false;
    }
    // If reallocation succeeded, memory may or may not have been moved
    // to fulfill the allocation request, invalidating output->data.
    output->data = data;
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!px4__msg__VehicleRoi__init(&output->data[i])) {
        // If initialization of any new item fails, roll back
        // all previously initialized items. Existing items
        // in output are to be left unmodified.
        for (; i-- > output->capacity; ) {
          px4__msg__VehicleRoi__fini(&output->data[i]);
        }
        return false;
      }
    }
    output->capacity = input->size;
  }
  output->size = input->size;
  for (size_t i = 0; i < input->size; ++i) {
    if (!px4__msg__VehicleRoi__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}
