import pandas as pd

def read_excel(file_path):
    df = pd.read_excel(file_path)

    # Convert all cells to text
    lines = []
    for col in df.columns:
        lines.extend(df[col].dropna().astype(str).tolist())

    return lines
