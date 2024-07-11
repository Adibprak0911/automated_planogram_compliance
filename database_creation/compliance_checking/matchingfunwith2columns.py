import pandas as pd

def planogram_compliance(detected_csv, planogram_csv):
    # Load the CSV files into DataFrames
    detected_df = pd.read_csv(detected_csv)
    planogram_df = pd.read_csv(planogram_csv)
    
    # Merge the DataFrames on ProductID to compare the ShelfID
    comparison_df = pd.merge(detected_df, planogram_df, on='ProductID', suffixes=('_detected', '_planogram'))
    
    # Calculate the number of correct placements
    correct_placements = (comparison_df['ShelfID_detected'] == comparison_df['ShelfID_planogram']).sum()
    
    # Calculate the total number of detected products
    total_detected = len(detected_df)
    
    # Calculate the accuracy rate
    accuracy_rate = correct_placements / total_detected
    
    # Get the ProductIDs of mismatched products
    mismatched_products = comparison_df[comparison_df['ShelfID_detected'] != comparison_df['ShelfID_planogram']]['ProductID'].tolist()
    
    return accuracy_rate, mismatched_products

# Example usage
detected_csv = 'detected_products.csv'
planogram_csv = 'default_planogram.csv'

accuracy_rate, mismatched_products = planogram_compliance(detected_csv, planogram_csv)
print(f'Accuracy Rate: {accuracy_rate * 100:.2f}%')
print(f'Mismatched Products: {mismatched_products}')