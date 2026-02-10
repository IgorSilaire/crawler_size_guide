# analyzer/product_attributes.py

import json


def extract_from_breadcrumbs(soup):
    """
    Extract breadcrumb items if present.
    Returns a list of strings.
    """
    crumbs = []

    # cas fréquents : nav/ol/ul avec 'breadcrumb' dans la classe
    for container in soup.find_all(["nav", "ol", "ul"]):
        classes = " ".join(container.get("class", [])).lower()
        if "breadcrumb" in classes:
            crumbs = [
                li.get_text(strip=True)
                for li in container.find_all("li")
                if li.get_text(strip=True)
            ]
            break

    return crumbs


def extract_from_json_ld(soup):
    """
    Extract Product structured data if present.
    Returns a dict.
    """
    for script in soup.find_all("script", type="application/ld+json"):
        try:
            data = json.loads(script.string)
            if isinstance(data, dict) and data.get("@type") == "Product":
                return data
        except Exception:
            continue

    return {}
