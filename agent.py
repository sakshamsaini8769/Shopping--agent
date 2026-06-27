import re

from prompts import SYSTEM_PROMPT
from tools import (
    search_products,
    scrape_product,
    calculate_discount,
    summarize_reviews,
)


def shopping_agent(user_query):
    """
    Main AI Shopping Agent
    """

    query = user_query.lower()

    # ----------------------------
    # Tool 1 : Search Product
    # ----------------------------
    if any(word in query for word in ["search", "buy", "best", "laptop", "mobile", "headphone", "product"]):

        results = search_products(user_query)

        return {
            "tool_used": "Product Search Tool",
            "result": results
        }

    # ----------------------------
    # Tool 2 : Website Scraper
    # ----------------------------
    elif query.startswith("http") or "www." in query:

        data = scrape_product(user_query)

        return {
            "tool_used": "Web Scraper",
            "result": data
        }

    # ----------------------------
    # Tool 3 : Discount Calculator
    # ----------------------------
    elif "discount" in query:

        numbers = re.findall(r"\d+", query)

        if len(numbers) >= 2:

            price = float(numbers[0])
            discount = float(numbers[1])

            return {
                "tool_used": "Discount Calculator",
                "result": calculate_discount(price, discount)
            }

        else:
            return {
                "tool_used": "Discount Calculator",
                "result": "Please enter: discount 50000 10"
            }

    # ----------------------------
    # Tool 4 : Review Summarizer
    # ----------------------------
    elif "review" in query or "summarize" in query:

        text = user_query.replace("summarize", "")

        summary = summarize_reviews(text)

        return {
            "tool_used": "Review Summarizer",
            "result": summary
        }

    # ----------------------------
    # Default
    # ----------------------------
    else:

        return {
            "tool_used": "None",
            "result": """
I can help with:

🔍 Search Products

🌐 Scrape Website

💰 Calculate Discount

📝 Summarize Reviews
"""
        }