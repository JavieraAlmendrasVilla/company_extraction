# main.py
import os
import requests
import csv
from tqdm import tqdm
import pandas as pd
from config import API_KEY, BASE_URL


# ---- Fetch Company ----
def fetch_company(
        query: str,
        features: list[str] | None = None,
):
    url = f"{BASE_URL}/fetch-organization"

    params = {"api_key": API_KEY, "q": query, "ai_search": "on-default"}

    # IMPORTANT: feature params must be repeated
    if features:
        if len(features) == 1:
            params["feature"] = features[0]
        else:
            # repeat for multiple features
            for i, feature in enumerate(features):
                params[f"feature[{i}]"] = feature

    response = requests.get(url, params=params)
    response.raise_for_status()
    response_json = response.json()
    return response_json


# ---- Extract Annual Financial Statements (STRUCTURED) ----
def extract_annual_statements(company_json):
    """
    Returns a list of rows:
    one row per company per year
    """

    rows = []

    company_name = (
            company_json.get("organization", {})
            .get("name")
            or company_json.get("name")
    )

    entity_id = company_json.get("entity_id")

    statements = company_json.get("annual_financial_statements", [])

    for stmt in statements:
        rows.append({
            "entity_id": entity_id,
            "company": company_name,
            "year": stmt.get("year"),
            "document_date": stmt.get("document_date"),
            "document_title": stmt.get("document_title"),
            "language": stmt.get("language"),
            "document_type": stmt.get("document_type"),
            "document_md": stmt.get("document_md"),
        })

    return rows


# ---- Batch Fetch ----
def fetch_companies_annuals(company_names):
    all_rows = []

    for name in tqdm(company_names):
        try:
            company = fetch_company(
                name,
                features=["annual_financial_statements"]
            )

            rows = extract_annual_statements(company)
            all_rows.extend(rows)

        except Exception as e:
            print(f"Error with {name}: {e}")

    return pd.DataFrame(all_rows)


# ---- Main ----
if __name__ == "__main__":
    company_names = [
        "Siemens AG",
        "BASF SE",
        # "OroraTech GmbH"
    ]

    df = fetch_companies_annuals(company_names)

    # ensure output directory exists
    os.makedirs("data/results", exist_ok=True)

    df.to_csv(
        "data/results/annual_financial_statements.csv",
        index=False,
        encoding="utf-8-sig",
        quoting=csv.QUOTE_ALL
    )

    print(f"Saved {len(df)} rows")
