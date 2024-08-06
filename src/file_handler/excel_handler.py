import pandas as pd

def extract_excel_data(file_path):
    df = pd.read_excel(file_path)
    return df.to_dict(orient='records')
