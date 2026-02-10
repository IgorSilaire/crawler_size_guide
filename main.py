from crawler.crawler import crawl
from analyzer.product_analyzer import analyze_product
from exporters.excel_exporter import create_excel

URLS = [
    "https://kleman-france.com/products/padror-th-cognac",
    "https://www.prada.com/fr/fr/p/blouson-en-re-nylon/SGD103_1WQ8_F0SVF_S_OOO"
]

results = []

for url in URLS:
    html = crawl(url, headless=False)  
    product_result = analyze_product(html, url)
    results.append(product_result)

create_excel(results)
