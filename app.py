import streamlit as st
from agent import shopping_agent

# ---------------------------
# Page Config
# ---------------------------
st.set_page_config(
    page_title="🛒 ShopSmart AI",
    page_icon="🛍️",
    layout="wide"
)

# ---------------------------
# Custom CSS
# ---------------------------
st.markdown("""
<style>

.main{
    background-color:#f5f5f5;
}

.title{
    font-size:40px;
    font-weight:bold;
    color:#ff4b4b;
}

.tool{
    background:#ffffff;
    padding:15px;
    border-radius:10px;
    margin-bottom:15px;
    box-shadow:0px 0px 8px rgba(0,0,0,0.1);
}

</style>
""", unsafe_allow_html=True)

# ---------------------------
# Header
# ---------------------------
st.markdown(
    "<p class='title'>🛒 ShopSmart AI Shopping Agent</p>",
    unsafe_allow_html=True
)

st.write("Find the best products with AI 🚀")

# ---------------------------
# Sidebar
# ---------------------------

st.sidebar.title("⚙ Filters")

budget = st.sidebar.slider(
    "Budget (₹)",
    1000,
    200000,
    50000
)

brand = st.sidebar.selectbox(
    "Preferred Brand",
    [
        "Any",
        "HP",
        "Dell",
        "Lenovo",
        "ASUS",
        "Acer",
        "Apple"
    ]
)

# ---------------------------
# User Input
# ---------------------------

query = st.text_input(
    "🔍 Search Product",
    placeholder="Example: Best gaming laptop under 70000"
)

# ---------------------------
# Search Button
# ---------------------------
from tools import recommend_product

if st.button("Search"):

    if query == "":

        st.warning("Please enter a product.")

    else:

        final_query = f"{query} under {budget} {brand}"

        response = shopping_agent(final_query)

        st.success(f"Tool Used : {response['tool_used']}")

        result = response["result"]

        # Search Results
        if isinstance(result, list):

            for item in result:

                st.markdown("---")

                st.subheader(item["title"])

                st.write(item["description"])

                st.markdown(
                    f"[Open Product]({item['link']})"
                )

        # Dictionary Result
        elif isinstance(result, dict):

            st.json(result)

        # Text Result
        else:

            st.write(result)

# ---------------------------
# Footer
# ---------------------------

st.markdown("---")

st.caption("Made with ❤️ using Streamlit + Gemini AI")