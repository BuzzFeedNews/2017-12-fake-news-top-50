#!/usr/bin/env python
import pandas as pd
from urllib.parse import urlparse
import sys
import re

def normalize_domain(domain):
    domain = domain.strip()
    if domain[:4] != "http":
        domain = "http://" + domain
    netloc = urlparse(domain).netloc
    clean = re.sub(r"^(www\.|en\.)", "", netloc).lower()
    return clean

# Sites, 2016
sys.stderr.write("Generating sites_2016.csv\n")

pd.read_excel(
    "data-raw/Fake news 2017.xlsx",
    sheet_name = "2016 Sites"
).rename(columns = {
    "URL": "url"
}).dropna(
    subset = [ "url" ]
).assign(
    domain = lambda x: x["url"].apply(normalize_domain)
).sort_values(
    "domain" 
)[[
    "domain"
]].to_csv(
    "data/sites_2016.csv",
    index = False
)

# Sites, 2017
sys.stderr.write("Generating sites_2017.csv\n")

pd.read_excel(
    "data-raw/Fake news 2017.xlsx",
    sheet_name = "2017 Sites"
).rename(columns = {
    "URL": "url",
    "Network": "network"
}).dropna(
    subset = [ "url" ]
).assign(
    domain = lambda x: x["url"].apply(normalize_domain),
    network = lambda x: x["network"].str.strip()
).sort_values(
    "domain" 
)[[
    "domain",
    "network"
]].to_csv(
    "data/sites_2017.csv",
    index = False
)

# Top 50 posts, 2016
sys.stderr.write("Generating top_2016.csv\n")

pd.read_excel(
    "data-raw/Fake news 2017.xlsx",
    sheet_name = "2016 Fakes"
).rename(columns = {
    "Headline": "title",
    "URL": "url",
    "Month Published": "month",
    "FB Enagements": "fb_engagements",
    "Category": "category" 
}).dropna(
    subset = [ "url" ]
).assign(
    domain = lambda x: x["url"].apply(normalize_domain),
    month = lambda x: x["month"].str.strip()
)[[
    "title",
    "url",
    "domain",
    "month",
    "fb_engagements",
    "category"
]].to_csv(
    "data/top_2016.csv",
    index = False
)

# Top 50 posts, 2017
sys.stderr.write("Generating top_2017.csv\n")

pd.read_excel(
    "data-raw/Fake news 2017.xlsx",
    sheet_name = "2017 Top 50"
).rename(columns = {
    "FB Engagements": "fb_engagements",
    "Category": "category" 
}).dropna(
    subset = [ "url" ]
).assign(
    domain = lambda x: x["url"].apply(normalize_domain)
)[[
    "title",
    "url",
    "domain",
    "fb_engagements",
    "published_date",
    "category"
]].to_csv(
    "data/top_2017.csv",
    index = False
)

# Top 50 fact checks.xlsx
sys.stderr.write("Generating fact_checks.csv\n")

pd.read_excel(
    "data-raw/Top 50 fact checks.xlsx",
    sheet_name = "Sheet1"
).rename(columns = {
    "Poltiifact FB": "Politifact FB",
}).dropna(
    subset=["url"]
)[[
    "title",
    "url",
    "Politifact",
    "Politifact FB",
    "Snopes",
    "Snopes FB",
    "Factcheck",
    "Factcheck FB",
    "ABC",
    "ABC FB"
]].to_csv(
    "data/fact_check.csv",
    index=False
)
