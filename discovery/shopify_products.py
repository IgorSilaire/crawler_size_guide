from urllib.parse import urlparse
from crawler.http_client import fetch_json

MAX_PRODUCTS = 5

def discover_shopify_products(collection_url: str) -> list[str]:
    api_url = collection_url.rstrip("/") + f"/products.json?limit={MAX_PRODUCTS}"
    data = fetch_json(api_url)

    base = "{uri.scheme}://{uri.netloc}".format(
        uri=urlparse(collection_url)
    )

    products = []
    for product in data.get("products", []):
        handle = product.get("handle")
        if handle:
            products.append(f"{base}/products/{handle}")

    return products
