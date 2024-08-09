import pandas as pd
import os
import logging

# Setup logging
logging.basicConfig(filename='logs/data_preparation.log', level=logging.INFO,
                    format='%(asctime)s:%(levelname)s:%(message)s')

# Define data paths
raw_data_path = 'data/raw/Data S7 BacteriaRawData.xlsx'
processed_data_path = 'data/processed/'

# Function to read and process all sheets
def read_and_process_excel(file_path):
    xls = pd.ExcelFile(file_path)
    all_sheets = {}
    for sheet_name in xls.sheet_names:
        df = pd.read_excel(xls, sheet_name=sheet_name, header=None)
        # Add your logic to name the columns here
        # df.columns = ['col1', 'col2', ..., 'colN']
        all_sheets[sheet_name] = df
        df.to_csv(os.path.join(processed_data_path, f'{sheet_name}.csv'), index=False)
        logging.info(f'Sheet {sheet_name} processed and saved to {processed_data_path}')
    return all_sheets

all_sheets = read_and_process_excel(raw_data_path)
