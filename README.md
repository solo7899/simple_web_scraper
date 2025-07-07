# Web Scraper

A simple Python web scraper that fetches and parses news headlines from [Hacker News](https://news.ycombinator.com/), outputting the results in JSON and/or CSV format.

## Features

- Fetches HTML content from a specified URL (default: Hacker News)
- Parses news titles and links
- Outputs results in JSON and/or CSV
- Verbose mode for detailed output

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

Run the scraper with optional arguments:

```sh
python scraper.py [--json] [--csv] [-v]
```

### Arguments

- `--json` Output results to `output.json`
- `--csv` Output results to `output.csv`
- `-v`, `--verbose` Enable verbose output

### Example

Fetch news and output both JSON and CSV with verbose logging:

```sh
python scraper.py --json --csv -v
```

## Output

- `output.json`: List of news items in JSON format
- `output.csv`: List of news items in CSV format

**Writer:** SOLO7899
