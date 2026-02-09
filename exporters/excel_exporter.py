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