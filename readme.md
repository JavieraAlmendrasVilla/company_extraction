# Automated Corporate Intelligence: German Annual Report Screening System

This project is an automated data engineering and NLP pipeline designed to fetch, process, and analyze official German corporate filings. By integrating with the [handelsregister.ai](https://handelsregister.ai/) API, the system transforms unstructured financial reports into actionable business intelligence, specifically focused on identifying strategic themes like ESG (Environmental, Social, and Governance) and sustainability initiatives.

## 🚀 Strategic Value

Manually reviewing thousands of annual reports is labor-intensive and error-prone. This system provides:

  * **Efficiency**: Rapidly extracts data from hundreds of companies in minutes.
  * **Competitive Intelligence**: Automatically flags keyword-specific statements (e.g., "Net Zero", "Supply Chain") across entire sectors.
  * **Data Consistency**: Converts varied PDF/Text filings into structured, queryable CSV datasets.

## 🛠️ Tech Stack

  * **Language**: Python 3.11
  * **Data Processing**: Pandas, NumPy
  * **API Integration**: REST API (Requests)
  * **Text Analysis**: NLP-based Keyword Extraction
  * **Engineering**: Modular pipeline design (Extraction → Transformation → Screening)

## 🏗️ Project Architecture

The system is divided into three functional modules to ensure scalability and maintainability:

```text
company_extraction/
├── main.py            # Extraction Engine: Fetches API data & structures financial statements
├── screening.py       # Analysis Engine: Processes extracted text for strategic keywords
├── config.py          # Security: Manages API credentials and environment variables
└── data/results/      # Output: Structured CSV datasets for stakeholder review
```

## ⚙️ Installation & Setup

1.  **Clone the Repository**

    ```bash
    git clone https://github.com/JavieraAlmendrasVilla/company_extraction.git
    cd company_extraction
    ```

2.  **Install Dependencies**

    ```bash
    pip install -r requirements.txt
    ```

3.  **Configure API Credentials**
    Create a `config.py` file in the root directory:

    ```python
    API_KEY = "YOUR_HANDELSREGISTER_API_KEY"
    BASE_URL = "https://handelsregister.ai/api/v1"
    ```

## 📈 Workflow

### 1\. Data Extraction (`main.py`)

Fetches annual reports for a target list of companies (e.g., Siemens AG, OroraTech GmbH). The engine outputs a comprehensive CSV (`annual_financial_statements.csv`) containing:

  * **Company Metadata**: Entity ID, Language, and Document Type.
  * **Full Text Content**: Raw document strings ready for analysis.

### 2\. Intelligent Screening (`screening.py`)

The screening engine parses the extracted data for high-impact keywords.

  * **Default Keywords**: `sustainability`, `net zero`, `green bond`, `supply chain`, `carbon footprint`.
  * **Output**: A finalized report (`screening_results.csv`) flagging specific hits and sentences where critical statements were made.

## 🧪 Roadmap

  * [ ] **Sentiment Analysis**: Integrate VADER or BERT to determine the "tone" of corporate sustainability claims.
  * [ ] **Multilingual Expansion**: Enhance screening for German-specific financial terminology.
  * [ ] **Visualization Dashboard**: Connect output to Tableau or Streamlit for real-time tracking.

-----

## 👤 Contact

[cite_start]**Javiera Almendras Villa** [cite: 1]


  * [cite_start]**GitHub**: [github.com/JavieraAlmendrasVilla](https://www.google.com/search?q=https://github.com/JavieraAlmendrasVilla) [cite: 1]
  * [cite_start]**Hugging Face**: [huggingface.co/javiialmendras/spaces](https://huggingface.co/javiialmendras/spaces) [cite: 2]
