import pandas as pd
import os 

folder_path = "Path to folder where is xlsx files"
files = [file for file in os.listdir(folder_path) if file.endswith('.xlsx')]
print(files)

dataframes = []
for file in files:
    df = pd.read_excel(os.path.join(folder_path, file))
    dataframes.append(df)

merged_df = pd.concat(dataframes)

output_path = "Path to folder where the merged file xlsx will be saved"
merged_df.to_excel(os.path.join(output_path, "merged_data.xlsx"), index=False)

