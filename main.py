from discovery.search_products import discover_shopify_products
from crawler.playwright_check import analyze_product_playwright
from exporters.excel_exporter import export_results

COLLECTION_URLS = [
    "https://kleman-france.com/collections/chaussures-derbies",
    "https://kleman-france.com/collections/chaussures-boots",
    "https://kleman-france.com/collections/accessoires-bonnets",
    "https://www.labottegardiane.com/collections/baskets",
    "https://www.labottegardiane.com/collections/sandales-femme",
    "https://www.labottegardiane.com/collections/sacs"
    #"https://www.prada.com/fr/fr/womens/shoes/c/10070EU"
    
]

results = []

for collection_url in COLLECTION_URLS:
    product_urls = discover_shopify_products(collection_url)

    for product_url in product_urls:
        try:
            result = analyze_product_playwright(product_url)
            results.append(result)
        except Exception:
            pass

export_results(results)
