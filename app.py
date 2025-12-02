import streamlit as st
import random

st.set_page_config(page_title="Pinterest Demo", layout="wide")
st.title("📌 Simple Pinterest-Style Demo")

# Some sample images (Unsplash placeholders)
image_urls = [
    "https://source.unsplash.com/400x600/?nature",
    "https://source.unsplash.com/400x500/?city",
    "https://source.unsplash.com/400x650/?travel",
    "https://source.unsplash.com/400x550/?art",
    "https://source.unsplash.com/400x700/?design",
    "https://source.unsplash.com/400x450/?food",
    "https://source.unsplash.com/400x620/?animals",
    "https://source.unsplash.com/400x580/?ocean",
]

# Create 3 uneven Pinterest-like columns
cols = st.columns(3)

for idx, url in enumerate(image_urls):
    col = cols[idx % 3]  # distribute images across columns
    with col:
        st.image(url, use_container_width=True)
        st.caption(f"Image #{idx+1}")

st.write("✨ This is a simple simulated Pinterest-style layout using Streamlit.")
