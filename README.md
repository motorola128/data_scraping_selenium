
# Mobile Data Scraper

A Python web scraping project that collects mobile phone information from [Smartprix](https://www.smartprix.com/mobiles) using Selenium and extracts structured specifications into a CSV dataset using BeautifulSoup and Pandas.

The project demonstrates browser automation, HTML parsing, regular expressions, data extraction, and basic data preparation.

## Project Overview

Mobile phone specifications are displayed across product listings on Smartprix. This project automates the process of loading the listings, interacting with page elements, collecting the rendered HTML, and extracting relevant information into a structured dataset.

The extracted data can be used for data cleaning, exploratory data analysis (EDA), visualization, and further data processing.

## Features

- **Browser automation:** Uses Selenium to open the Smartprix mobile listings page.
- **Page interaction:** Automatically interacts with page filters and the load-more control.
- **Dynamic content handling:** Waits for page elements and scrolls to relevant controls.
- **HTML extraction:** Saves the rendered page source to an HTML file.
- **Specification extraction:** Uses BeautifulSoup and regular expressions to identify mobile specifications.
- **Data organization:** Stores extracted records in a Pandas DataFrame.
- **CSV export:** Saves the resulting dataset for further analysis.
- **Missing-value handling:** Uses NumPy to represent unavailable or unmatched specifications.

## Technologies Used

| Technology | Purpose |
|---|---|
| Python | Main programming language |
| Selenium | Browser automation and page interaction |
| Google Chrome | Browser used for scraping |
| BeautifulSoup | HTML parsing and data extraction |
| Regular Expressions (`re`) | Matching specification text |
| Pandas | Data organization and CSV export |
| NumPy | Handling missing values |
| Jupyter Notebook | Interactive development and exploration |

## Project Structure

```text
data_scraping_selenium/
│
├── scraper.py              # Selenium browser automation
├── selenium_scraping.ipynb # HTML parsing and data extraction
├── scraper.csv             # Extracted mobile specifications
├── smartprix.html          # Saved HTML source (generated locally)
└── README.md               # Project documentation
```

Note: `smartprix.html` is generated when the scraper runs. It may not be included in the repository.

## Extracted Data

The dataset contains the following columns:

| Column | Description |
|---|---|
| `name` | Mobile phone name |
| `price` | Listed price |
| `rating` | Score extracted from the product listing |
| `sim` | SIM-related specifications |
| `processor` | Processor information |
| `ram` | RAM and internal storage details |
| `battery` | Battery specifications |
| `display` | Display specifications |
| `camera` | Camera specifications |
| `card` | Memory card information |
| `os` | Operating system information |

Some values may be missing because a specification is not listed or does not match the extraction pattern. The `rating` column represents the extracted score, not necessarily a customer review rating.

## Getting Started

### Prerequisites

Install the following before running the project:

- Python 3.9 or later
- Google Chrome
- Jupyter Notebook (if running the notebook)
- A compatible Selenium browser driver setup

### 1. Clone the repository

```bash
git clone https://github.com/motorola128/data_scraping_selenium.git
cd data_scraping_selenium
```

### 2. Install the dependencies

```bash
pip install selenium beautifulsoup4 pandas numpy jupyter
```

### 3. Run the Selenium scraper

Execute:

```bash
python scraper.py
```

The script opens Smartprix, interacts with the listing page, attempts to load additional products, and saves the rendered HTML to `smartprix.html`.

Make sure the browser driver is configured correctly. Recent Selenium versions can often manage the appropriate driver automatically when Chrome is installed and accessible.

### 4. Extract the specifications

Launch Jupyter Notebook:

```bash
jupyter notebook
```

Open `selenium_scraping.ipynb` and run its cells to parse the saved HTML, extract the mobile specifications, and generate the CSV output.

Ensure the HTML file exists in the location expected by the notebook.

## Output

The extracted data is stored in:

```text
scraper.csv
```

The CSV file can be opened with Pandas, Excel, or other data analysis tools.

Example:

```python
import pandas as pd

df = pd.read_csv("scraper.csv")

print(df.head())
print(df.info())
print(df.isna().sum())
```

These commands display sample records, column data types, and the number of missing values in each column.

## Learning Outcomes

Through this project, I practised:

- Automating browser interactions with Selenium.
- Locating webpage elements using XPath.
- Waiting for elements and handling dynamic page interactions.
- Extracting HTML using Selenium's `page_source`.
- Parsing HTML with BeautifulSoup.
- Using regular expressions to match specifications.
- Structuring extracted data with Pandas.
- Identifying missing values in a dataset.
- Exporting data to CSV for downstream analysis.

## Future Improvements

- Improve XPath selectors to make the scraper more resilient to website layout changes.
- Add robust exception handling and logging.
- Improve pagination and loading-completion checks.
- Refine regular expressions to recognize more specification formats.
- Improve missing-value analysis and data type conversion.
- Add exploratory data analysis and visualizations.
- Explore storing the extracted data in a PostgreSQL database.

## Responsible Use

This project is intended for educational purposes. Before collecting data directly from Smartprix, review its current terms of service and applicable access restrictions. Respect rate limits, avoid overloading the website, and obtain permission where required before redistributing collected content.


