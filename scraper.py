import argparse
import csv
import json
import requests

from bs4 import BeautifulSoup

def cmd():
    parser = argparse.ArgumentParser(description="A simple web scraper to fetch and parse HTML content.")
    parser.add_argument("-v", "--verbose", action="store_true", help="Enable verbose output")
    parser.add_argument("--json", action="store_true", help="Output results in JSON format")
    parser.add_argument("--csv", action="store_true", help="Output results in CSV format")
    return parser.parse_args()

def get_html(url):
    """
    Fetches the HTML content of a given URL.

    Args:
        url (str): The URL to fetch.

    Returns:
        str: The HTML content of the page.
    """
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad responses
        return response.text
    except requests.RequestException as e:
        print(f"Error fetching {url}: {e}")
        return None


def parse_html(html_content, verbose=False):
    """
    Parses the HTML content and extracts relevant information.

    Args:
        html_content (str): The HTML content to parse.

    Returns:
        list: A list of dictionaries containing extracted data.
    """
    soup = BeautifulSoup(html_content, 'html.parser')
    items = []

    news = soup.find_all('span', class_='titleline')
    if verbose:
        print(f"Found {len(news)} news items.")
    for item in news:
        title = item.a.text
        link = item.a['href']
        if verbose:
            print(f"Title: {title}, Link: {link}")
        items.append({'title': title, 'link': link})
    return items


def output_json(data, verbose=False):
    """
    Outputs the data in JSON format.

    Args:
        data (list): The data to output.
    """
    if verbose:
        print("Outputting data in JSON format.")
    json.dump(data, open('output.json', 'w'), indent=4)


def output_csv(data, verbose=False):
    """
    Outputs the data in CSV format.

    Args:
        data (list): The data to output.
    """
    if verbose:
        print("Outputting data in CSV format.")
    with open('output.csv', 'w', newline='') as csvfile:
        fieldnames = ['title', 'link']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for item in data:
            writer.writerow(item)


if __name__ == "__main__":
    args = cmd()

    url = "https://news.ycombinator.com/"
    html_content = get_html(url)
    if html_content:
        print(f"Fetched {len(html_content)} characters from {url}")
    else:
        print("Failed to fetch the HTML content.")
        exit(1)
    
    news_links = parse_html(html_content, args.verbose)

    if args.json:
        output_json(news_links, args.verbose)
    if args.csv:
        output_csv(news_links, args.verbose)
