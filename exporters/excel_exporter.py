"""
Docstring for exporters.excel_exporter
import pandas as pd
from pathlib import Path

def create_excel(results: list, output_path: str = "output/size_guides.xlsx"):
    
    Path(output_path).parent.mkdir(parents=True, exist_ok=True)
    
    rows= []
    
    for result in results:
        rows.append({
            "Nom Produit": result.get("product_name"),
            "Gender": result.get("gender"),
            "Type": result.get("product_type"),
            "URL": result.get("product_url"),
            "Guide de taille": result.get("has_size_guide"),
        })

    df = pd.DataFrame(rows)
    df.to_excel(output_path, index=False)
"""

import pandas as pd
from pathlib import Path

def export_results(results: list, output="output/size_guides.xlsx"):
    Path("output").mkdir(exist_ok=True)

    df = pd.DataFrame(results)
    df.to_excel(output, index=False)
