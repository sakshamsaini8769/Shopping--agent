from duckduckgo_search import DDGS
import google.generativeai as genai
import os
from dotenv import load_dotenv
from prompts import SYSTEM_PROMPT

from scraper import scrape_website

# Load API Key
load_dotenv()

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

model = genai.GenerativeModel("gemini-1.5-flash")


# -----------------------------
# Tool 1 - Product Search
# -----------------------------
def search_products(query):
    """
    Search products using DuckDuckGo.
    """

    results = []

    with DDGS() as ddgs:
        search_results = ddgs.text(query, max_results=5)

        for item in search_results:
            results.append({
                "title": item["title"],
                "link": item["href"],
                "description": item["body"]
            })

    return results


# -----------------------------
# Tool 2 - Website Scraper
# -----------------------------
def scrape_product(url):
    """
    Scrape website content.
    """
    return scrape_website(url)


# -----------------------------
# Tool 3 - Discount Calculator
# -----------------------------
def calculate_discount(price, discount):

    final_price = price - (price * discount / 100)

    return {
        "Original Price": price,
        "Discount": discount,
        "Final Price": round(final_price, 2)
    }


# -----------------------------
# Tool 4 - AI Review Summarizer
# -----------------------------
def summarize_reviews(review_text):

    prompt = f"""
{SYSTEM_PROMPT}

Product Reviews:

{review_text}

Summarize in the following format:

✅ Pros

❌ Cons

⭐ Overall Recommendation
"""

    response = model.generate_content(prompt)

    return response.text

    from prompts import SYSTEM_PROMPT

    return response.text
from prompts import SYSTEM_PROMPT

def recommend_product(search_results, budget):

    prompt = f"""
{SYSTEM_PROMPT}

Budget: ₹{budget}

Search Results:

{search_results}

Recommend the best product.

Explain:

1. Best Product
2. Why?
3. Pros
4. Cons
5. Final Verdict
"""

    response = model.generate_content(prompt)

    return response.text