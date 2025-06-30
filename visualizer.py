import streamlit as st

LABEL_COLORS = {
    "CARDINAL": "#f9c74f",     # yellow-orange
    "DATE": "#90be6d",         # green
    "EVENT": "#f94144",        # red
    "FAC": "#577590",          # steel blue
    "GPE": "#f9844a",          # orange
    "LANGUAGE": "#43aa8b",     # teal
    "LAW": "#277da1",          # blue
    "LOC": "#f3722c",          # coral
    "MONEY": "#4d908e",        # dark cyan
    "NORP": "#bc5090",         # magenta
    "ORDINAL": "#ffafcc",      # light pink
    "ORG": "#9e2a2b",          # maroon
    "PERCENT": "#ef476f",      # rose
    "PERSON": "#118ab2",       # strong blue
    "PRODUCT": "#8ecae6",      # sky blue
    "QUANTITY": "#6a4c93",     # purple
    "TIME": "#00b4d8",         # cyan
    "WORK_OF_ART": "#e76f51",  # rust
    "DEFAULT": "#e0e0e0",
}

def render_entities(text, entities):
    """Render text with highlighted entities using HTML."""
    offset = 0
    for ent in sorted(entities, key=lambda x: x["start"]):
        label = ent["entity_group"]
        color = LABEL_COLORS.get(label, LABEL_COLORS["DEFAULT"])
        start, end = ent["start"] + offset, ent["end"] + offset
        original = text[start:end]
        span = f"<span style='background-color:{color}; padding:2px 4px; border-radius:4px;'>{original} <strong>[{label}]</strong></span>"
        text = text[:start] + span + text[end:]
        offset += len(span) - (end - start)

    st.markdown(f"<div style='line-height:1.8; font-size:16px'>{text}</div>", unsafe_allow_html=True)