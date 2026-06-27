Books Scraper Basic

A Python web scraper that collects data from [books.toscrape.com](https://books.toscrape.com) and saves it to a clean Excel file.

---

What It Does

- Scrapes the first page of books.toscrape.com
- Collects 3 data points for each of the 20 books
- Saves everything to a clean Excel file instantly

---

Data Collected

| Column | Description |
|---|---|
| Title | Full title of the book |
| Price | Price in GBP |
| Rating | Star rating (One to Five) |

---

Built With

- Python 3.11
- BeautifulSoup4 — for parsing HTML
- Requests — for fetching web pages
- Pandas — for saving data to Excel
- Openpyxl — for Excel file support

---

How to Run

*Step 1 — Install required libraries:
```
pip install requests beautifulsoup4 pandas openpyxl
```

*Step 2 — Run the scraper:
```
python Books_with_rating.py
```

*Step 3 — Check output:
A file called `books_data.xlsx` will be created in the same folder.

---

Project Files

| File | Description |
|---|---|
| `Books_with_rating.py` | Main scraper script |
| `books_data.xlsx` | Sample output Excel file |
| `README.md` | Project documentation |

---

Sample Output

| Title | Price | Rating |
|---|---|---|---|---|
| A Light in the Attic | £51.77 | Three |
| Tipping the Velvet | £53.74 | One |
| Soumission | £50.10 | One |

---

About

Built by Aryan — BS Computer Engineering Student, COMSATS University Islamabad.
Specializing in Python web scraping and automation.