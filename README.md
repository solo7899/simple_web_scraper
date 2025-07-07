# Web Scraper

A flexible Python web scraper for extracting data from any website by specifying the URL, HTML tag, and either a class or ID. Outputs results in JSON and/or CSV format with customizable filenames.

## Features

- Scrape any website by providing the URL
- Extract data using a specified HTML tag and either a class or ID
- Output results to custom-named JSON and/or CSV files
- Verbose mode for detailed logging

## Requirements

- Python 3.7+
- See `requirements.txt` for dependencies

## Installation

1. Clone this repository:
   ```sh
   git clone https://github.com/yourusername/web_scraper.git
   cd web_scraper
   ```
2. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```

## Usage

Run the scraper with the required and optional arguments:

```sh
python scraper.py --url <URL> --tag <TAG> [--clas <CLASS>] [--id <ID>] [--json <JSON_FILE>] [--csv <CSV_FILE>] [-v]
```

### Arguments

- `--url`, `-u` URL to scrape (**required**)
- `--tag` HTML tag to search for (**required**)
- `--clas` HTML class to search for (optional)
- `--id` HTML ID to search for (optional)
- `--json` Output results to specified JSON file (optional)
- `--csv` Output results to specified CSV file (optional)
- `-v`, `--verbose` Enable verbose output (optional)

**Note:** You must specify either `--clas` or `--id` for parsing.

### Example

Scrape all `<span>` elements with class `titleline` from Hacker News and output to `hn.json` and `hn.csv`:

```sh
python scraper.py --url https://news.ycombinator.com/ --tag span --clas titleline --json hn.json --csv hn.csv -v
```

## Output

- JSON and/or CSV files with extracted data (custom filenames)

---

**Writer:** SOLO7899
