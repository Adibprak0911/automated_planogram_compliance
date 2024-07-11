# #!/home/user/anaconda3/base/bin/python
# import pandas as pd
# def create_sample_planogram(file_path):
#     # Sample data for the planogram in the desired format
#     data = {
#         'Row 1': ['1001', '1002', '1004', '1010', '1007', '1032'],
#         'Row 2': ['2020', '2003', '2001', '2019', '2004'],
#         'Row 3': ['3005', '3010', '3001', '3015', '3003', '3020'],
#         # Add more rows as needed
#     }

#     # Convert the dictionary to a DataFrame and transpose it
#     planogram_df = pd.DataFrame(dict([(k, pd.Series(v)) for k, v in data.items()]))
    
#     # Save to CSV at the specified path without index and header
#     planogram_df.to_csv(file_path, index=False, header=False)

#     print(f"Sample planogram CSV file created successfully at {file_path}.")

# # Example usage
# file_path = 'database_creation/default_planogram.csv'
# create_sample_planogram(file_path)
# #/home/user/Documents/automated_planogram_compliance-1/database_creation

import pandas as pd

def create_sample_planogram(file_path):
    # Sample data for the planogram in the desired format
    data = {
        'Row 1': ['1001', '1002', '1004', '1010', '1007', '1032'],
        'Row 2': ['2020', '2003', '2001', '2019', '2004'],
        'Row 3': ['3005', '3010', '3001', '3015', '3003', '3020'],
        # Add more rows as needed
    }

    # Create a list of lists where each inner list is a row of product IDs
    rows = [[', '.join(v)] for k, v in data.items()]

    # Create a DataFrame
    planogram_df = pd.DataFrame(rows)

    # Save to CSV at the specified path without index and header
    planogram_df.to_csv(file_path, index=False, header=False)

    print(f"Sample planogram CSV file created successfully at {file_path}.")

# Example usage
file_path = 'database_creation/default_planogram.csv'
create_sample_planogram(file_path)
