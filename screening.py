import pandas as pd
import re

# Load CSV
df = pd.read_csv("data/results/annual_financial_statements.csv", encoding="utf-8-sig")

# Define keywords/phrases you care about
KEYWORDS = [
    "sustainability",
    "net zero",
    "green bond",
    "supply chain",
    "carbon footprint",
]


# Function to find hits in a text
def screen_text(text, keywords):
    hits = []
    for kw in keywords:
        # case-insensitive word boundary search
        pattern = r"\b" + re.escape(kw.lower()) + r"\b"
        if re.search(pattern, text.lower()):
            hits.append(kw)
    return hits


# Apply screening
results = []

for _, row in df.iterrows():
    text = row["document_md"]
    hits = screen_text(text, KEYWORDS)
    if hits:
        results.append({
            "entity_id": row["entity_id"],
            "company": row["company"],
            "year": row["year"],
            "document_title": row["document_title"],
            "keywords_found": ", ".join(hits)
        })

if __name__ == "__main__":
    # Convert to DataFrame
    screened_df = pd.DataFrame(results)

    # Save results
    screened_df.to_csv("data/results/screening_results.csv", index=False, encoding="utf-8-sig")
    print(f"Screened {len(screened_df)} rows")
