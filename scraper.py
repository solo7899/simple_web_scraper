import argparse
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


def parse_html(html_content):
    """
    Parses the HTML content and extracts relevant information.

    Args:
        html_content (str): The HTML content to parse.

    Returns:
        list: A list of dictionaries containing extracted data.
    """
    soup = BeautifulSoup(html_content, 'html.parser')
    items = []

    for item in soup.find_all('span', class_='titleline'):
        title = item.a.text
        link = item.a['href']
        items.append({'title': title, 'link': link})
    return items


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
