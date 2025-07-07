import argparse
import csv
import json
import requests

from bs4 import BeautifulSoup

def cmd():
    parser = argparse.ArgumentParser(description="A simple web scraper to fetch and parse HTML content.")
    parser.add_argument("--url", "-u", type=str, help="URL to scrape ")
    parser.add_argument("--tag", type=str, help="HTML tag to search for news items ")
    parser.add_argument("--clas", type=str, help="HTML class to search for news items")
    parser.add_argument("--id", type=str, help="HTML ID to search for news items")
    parser.add_argument("-v", "--verbose", action="store_true", help="Enable verbose output")
    parser.add_argument("--json", type=str, default=None, help="Output results in JSON format")
    parser.add_argument("--csv", type=str, default=None, help="Output results in CSV format")
    return parser.parse_args()

def get_html(url, verbose=False):
    """
    Fetches the HTML content of a given URL.

    Args:
        url (str): The URL to fetch.

    Returns:
        str: The HTML content of the page.
    """
    try:
        if verbose:
            print(f"Fetching HTML content from {url}")
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad responses
        return response.text
    except requests.RequestException as e:
        print(f"Error fetching {url}: {e}")
        return None


def parse_html_with_class(html_content, tag, class_, verbose=False):
    """
    Parses the HTML content and extracts relevant information.

    Args:
        html_content (str): The HTML content to parse.

    Returns:
        list: A list of dictionaries containing extracted data.
    """
    soup = BeautifulSoup(html_content, 'html.parser')
    items = []

    news = soup.find_all(tag, class_= class_)
    if verbose:
        print(f"Found {len(news)} news items.")
    for item in news:
        title = item.a.text
        link = item.a['href']
        if verbose:
            print(f"Title: {title}, Link: {link}")
        items.append({'title': title, 'link': link})
    return items


def parse_html_with_id(html_content, tag, id_, verbose=False):
    """
    Parses the HTML content and extracts relevant information using an ID.

    Args:
        html_content (str): The HTML content to parse.

    Returns:
        list: A list of dictionaries containing extracted data.
    """
    if tag is None:
        tag = "titleline"

    soup = BeautifulSoup(html_content, 'html.parser')
    items = []

    news = soup.find_all(tag, id_=id_)
    if verbose:
        print(f"Found {len(news)} news items.")
    for item in news:
        title = item.a.text
        link = item.a['href']
        if verbose:
            print(f"Title: {title}, Link: {link}")
        items.append({'title': title, 'link': link})
    return items


def output_json(data, json_name, verbose=False):
    """
    Outputs the data in JSON format.

    Args:
        data (list): The data to output.
    """
    if verbose:
        print("Outputting data in JSON format.")
    json.dump(data, open(json_name, 'w'), indent=4)


def output_csv(data, csv_name, verbose=False):
    """
    Outputs the data in CSV format.

    Args:
        data (list): The data to output.
    """
    if verbose:
        print("Outputting data in CSV format.")
    with open(csv_name, 'w', newline='') as csvfile:
        fieldnames = ['title', 'link']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for item in data:
            writer.writerow(item)


if __name__ == "__main__":
    args = cmd()

    if args.url is None:
        print("No URL provided.")
        exit(1)
    html_content = get_html(args.url, args.verbose)
    if html_content:
        print(f"Fetched {len(html_content)} characters from {args.url}")
    else:
        print("Failed to fetch the HTML content.")
        exit(1)
    
    if args.tag is None:
        print("No tag specified")
        exit(1)
    if args.clas:
        news_links = parse_html_with_class(html_content, args.tag, args.clas, args.verbose)
    elif args.id:
       news_links = parse_html_with_id(html_content, args.tag, args.id, args.verbose) 
    else:
        print("No class or ID specified for parsing")
        exit(1)

    if args.json:
        output_json(news_links, args.json, args.verbose)
    if args.csv:
        output_csv(news_links, args.csv , args.verbose)
