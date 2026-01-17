---

# Company Annual Report Screening

This project fetches annual reports of German companies from [handelsregister.ai](https://handelsregister.ai/), extracts structured financial statements, and screens them for keywords or statements relevant to your business offerings.

---

## Project Structure

```
company_extraction/
├── main.py                # Fetches company data & saves annual financial statements
├── screening.py           # Screens saved annual reports for keywords / phrases
├── config.py              # Stores API_KEY and BASE_URL
├── data/
│   └── results/           # Output CSV files
├── README.md              # This file
```

---

## Setup

1. **Clone the project**:

```bash
git clone https://github.com/JavieraAlmendrasVilla/company_extraction.git
cd company_extraction
```

2. **Install dependencies**:

```bash
pip install pandas requests tqdm
```

3. **Configure API key**:

Create a file `config.py` in the project root with:

```python
API_KEY = "YOUR_HANDLESREGISTER_API_KEY"
BASE_URL = "https://handelsregister.ai/api/v1"
```

Replace `"YOUR_HANDLESREGISTER_API_KEY"` with your actual API key.

---

## Step 1: Fetch Annual Reports

Run `main.py` to fetch annual financial statements for a list of companies and save them to CSV:

```bash
python main.py
```

* The list of companies can be modified in `main.py` under:

```python
company_names = [
    "Siemens AG",
    "OroraTech GmbH"
]
```

* Output CSV:

```
data/results/annual_financial_statements.csv
```

Columns include:

* `entity_id`
* `company`
* `year`
* `document_title`
* `document_md` (full report text)
* `language`
* `document_type`

---

## Step 2: Screen Reports for Keywords

Run `screening.py` to search the CSV for keywords or phrases relevant to your business:

```bash
python screening.py
```

* Define your keywords in `screening.py`:

```python
KEYWORDS = [
    "sustainability",
    "net zero",
    "green bond",
    "supply chain",
    "carbon footprint"
]
```

* The script will create a CSV:

```
data/results/screening_results.csv
```

* Columns include:

  * `entity_id`
  * `company`
  * `year`
  * `document_title`
  * `keywords_found` (or `hit_sentences` if sentence extraction is enabled)

---

## Optional Enhancements

* Extract **sentences containing keywords** for context.
* Process **thousands of companies** using batch processing or chunked reads.
* Use **semantic search / embeddings** for more intelligent screening beyond exact keywords.
* Split `document_md` into sections (balance sheet, P&L, notes) for structured analysis.

---

## Notes

* Ensure your output directories exist:

```python
os.makedirs("data/results", exist_ok=True)
```

* Use **UTF-8 encoding** for CSV to handle German characters correctly.

* Handle API credits carefully — fetching annual reports consumes credits.


