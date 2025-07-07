import requests

from bs4 import BeautifulSoup

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





    
if __name__ == "__main__":
    url = "https://news.ycombinator.com/"
    html_content = get_html(url)
    if html_content:
        print(f"Fetched {len(html_content)} characters from {url}")
    else:
        print("Failed to fetch the HTML content.")
        exit(1)
    
