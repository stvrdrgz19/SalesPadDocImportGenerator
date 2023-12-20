import pandas as pd
import os

# path of the xlsx files to combine
path = 'output'

# initialize an empty dataframe to store the combined data
# combined_df = utils.df

dfs = []

# iterate over the files in the specified path
for filename in os.listdir(path):
    if filename.endswith('.xlsx'):
        file_path = os.path.join(path, filename)

        # read the xlsx file into a dataframe
        df = pd.read_excel(file_path)

        # append the data to the dfs list
        dfs.append(df)

combined_df = pd.concat(dfs, ignore_index = True)

# output the combined data to a new xlsx sheet
combined_df.to_excel(f"output/Combined_Import.xlsx", index = False, sheet_name = "Sheet1")