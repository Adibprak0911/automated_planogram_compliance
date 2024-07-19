import streamlit as st
import pandas as pd
from odf.opendocument import OpenDocumentSpreadsheet
from odf.table import Table, TableRow, TableCell
from odf.text import P

# Define the Streamlit app
def main():
    st.title("**Planogram Compliance**")
    st.subheader("Choose your Walmart")
    
    # Dropdown for Walmart selection
    walmart_choice = st.selectbox("Select Walmart", ["Walmart A", "Walmart B", "Walmart C"])
    
    # Dropdown for number of items
    num_items = st.selectbox("Number of items", [1, 2, 3, 4])
    
    # Placeholder for item inputs
    item_details = []
    
    for i in range(num_items):
        st.subheader(f"Item {i+1} Details")
        model_name = st.text_input(f"Model Name for Item {i+1}")
        x = st.number_input(f"X for Item {i+1}")
        y = st.number_input(f"Y for Item {i+1}")
        z = st.number_input(f"Z for Item {i+1}")
        r = st.number_input(f"R for Item {i+1}")
        p = st.number_input(f"P for Item {i+1}")
        y_orientation = st.number_input(f"Y (Yaw) for Item {i+1}")
        selected = st.selectbox(f"Selected for Item {i+1}", [0, 1])
        
        item_details.append({
            "Model Name": model_name,
            "X": x,
            "Y": y,
            "Z": z,
            "R": r,
            "P": p,
            "Y (Yaw)": y_orientation,
            "Selected": selected
        })
    
    # Done button to save details to ODS file
    if st.button("Done"):
        save_to_ods(item_details)
        st.success("Details saved to planogram.ods")

# Function to save details to ODS file
def save_to_ods(item_details):
    ods = OpenDocumentSpreadsheet()
    table = Table(name="Planogram Compliance")

    # Define table headers
    headers = ["Model Name", "X", "Y", "Z", "R", "P", "Y (Yaw)", "Selected"]
    header_row = TableRow()
    for header in headers:
        cell = TableCell()
        cell.addElement(P(text=header))
        header_row.addElement(cell)
    table.addElement(header_row)
    
    # Add item details to the table
    for item in item_details:
        row = TableRow()
        for header in headers:
            cell = TableCell()
            cell.addElement(P(text=str(item[header])))
            row.addElement(cell)
        table.addElement(row)
    
    ods.spreadsheet.addElement(table)
    ods.save("planogram.ods")

if __name__ == "__main__":
    main()
