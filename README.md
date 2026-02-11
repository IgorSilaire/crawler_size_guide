# Size Guide Detection – Study Case (Fitle)

##  Project Overview


Objective:  
Automatically explore products sold on an e-commerce website and determine whether a size guide is available for each product.

The program:

- Discovers product URLs
- Visits each product page
- Detects the presence of a size guide
- Extracts basic product information
- Generates a structured Excel report

##  Goal

For each analyzed product:

- Retrieve product name
- Retrieve product gender (if applicable)
- Retrieve product URL
- Detect if a size guide exists

Output example:

| product_name | gender | product_url | has_size_guide |
|-------------|--------|-------------|----------------|
| Padror Noir | Homme | https://... | TRUE |


##  Detection Strategy

The program uses a 2 approach:

### 1️ HTTP Requests (requests)

Used for:

- Fast discovery of product URLs
- Lightweight site exploration


### 2️ Playwright (playwright)

Used for:

- Visiting product pages
- Accessing the final rendered DOM
- Detecting interactive elements (size guide buttons / triggers)

Why Playwright?

Many modern e-commerce websites:

- Load content dynamically
- Display size guides via modals
- Hide elements behind JavaScript interactions

##  Project Structure

study_case_fitle/

├── main.py  
├── requirements.txt  

├── config/  
│   └── keywords.py  

├── crawler/  
│   ├── http_client.py  
│   └── playwright_check.py  

├── discovery/  
│   └── search_products.py  

├── exporters/  
│   └── excel_exporter.py  

└── output/  
    └── size_guides.xlsx  

##  Installation

### 1️ Install dependencies

pip install -r requirements.txt

### 2️ Install Playwright browsers

playwright install


## Usage

Run the program:

python main.py

The Excel report will be generated in:

/output/size_guides.xlsx


##  How Size Guides Are Detected ?

A product is considered to have a size guide if the rendered page contains:

- A button
- A link
- Or a trigger element

Matching predefined keywords:

Examples:

- "Guide des tailles"
- "Size guide"
- "Size chart"

Keywords are centralized in:

config/keywords.py

## Limitations

Some websites may restrict automated exploration:

Examples:

- Heavy JavaScript rendering
- Anti-bot protections
- Non-public catalog APIs

Luxury / protected websites (e.g. Prada) may require:

- Dedicated extraction rules
- Alternative discovery strategies


