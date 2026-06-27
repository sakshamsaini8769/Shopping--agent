def format_price(price):
    return f"₹{price:,.2f}"


def clean_text(text):
    return text.replace("\n", " ").strip()


def calculate_savings(original_price, final_price):
    return original_price - final_price