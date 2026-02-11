import pandas as pd
from pathlib import Path

def export_results(results: list, output="output/size_guides.xlsx"):
    Path("output").mkdir(exist_ok=True)

    df = pd.DataFrame(results)
    df.to_excel(output, index=False)
