import streamlit as st
from ner_pipeline import load_pipeline,get_entities
from visualizer import render_entities

st.set_page_config(page_title="NER Tagger", layout="wide")
st.title("🧠 Named Entity Recognition")
st.markdown("Enter text below and extract named entities using your custom model.")

ner_pipeline = load_pipeline()


st.markdown("**Example:** Barack Obama was born in Hawaii and worked at the White House.")
text = st.text_area("✍️ Input Text", height=200, placeholder="Type or paste text here...")

# Run NER
if st.button("🔍 Extract Entities"):
    if text.strip():
        with st.spinner("Analyzing..."):
            entities = get_entities(text, ner_pipeline)     

            if not entities:
                st.warning("⚠️ No entities found. Try entering a more specific sentence with known names, places, or organizations.")
            else:
                render_entities(text, entities)
    else:
        st.warning("⚠️ Please enter some text.")
