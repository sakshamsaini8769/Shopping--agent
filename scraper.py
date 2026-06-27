import requests
from bs4 import BeautifulSoup


def scrape_website(url):
    """
    Scrapes a webpage and returns its title and visible text.
    """

    try:
        headers = {
            "User-Agent": (
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                "AppleWebKit/537.36 (KHTML, like Gecko) "
                "Chrome/125.0 Safari/537.36"
            )
        }

        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, "html.parser")

        title = soup.title.string if soup.title else "No Title"

        text = soup.get_text(separator=" ", strip=True)

        # Limit text length
        text = text[:3000]

        return {
            "title": title,
            "content": text
        }

    except Exception as e:
        return {
            "error": str(e)
        }