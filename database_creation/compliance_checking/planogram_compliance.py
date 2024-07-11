import pandas as pd

def planogram_compliance(detected_csv, planogram_csv):
    # Load the CSV files into DataFrames
    detected_df = pd.read_csv(detected_csv, header=None, names=['ProductID'])
    planogram_df = pd.read_csv(planogram_csv, header=None, names=['ProductID'])
    
    # Ensure the DataFrames have the same number of rows
    if len(detected_df) != len(planogram_df):
        raise ValueError("Detected products and planogram files must have the same number of products.")
    
    # Calculate the number of correct placements
    correct_placements = (detected_df['ProductID'] == planogram_df['ProductID']).sum()
    
    # Calculate the total number of detected products
    total_detected = len(detected_df)
    
    # Calculate the accuracy rate
    accuracy_rate = correct_placements / total_detected
    
    # Get the ProductIDs of mismatched products
    mismatched_products = detected_df[detected_df['ProductID'] != planogram_df['ProductID']]['ProductID'].tolist()
    
    return accuracy_rate, mismatched_products

# Example usage
detected_csv = 'detected_products.csv'
planogram_csv = 'default_planogram.csv'

accuracy_rate, mismatched_products = planogram_compliance(detected_csv, planogram_csv)
print(f'Accuracy Rate: {accuracy_rate * 100:.2f}%')
print(f'Mismatched Products: {mismatched_products}')