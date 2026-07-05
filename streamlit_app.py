"""
NHS Continuing Healthcare — Decision Support Tool (interactive questionnaire)

A public Streamlit app that presents each of the 12 DST care domains as a
plain-English question, builds the assessed-levels-of-need matrix, shows an
indicative conclusion, and lets the user download a completed PDF.

The entire questionnaire is a self-contained HTML/JS file (dst_app.html) that
runs in the browser — including PDF generation via a bundled copy of jsPDF —
so no data is sent to any server.

Run locally:
    pip install streamlit
    streamlit run streamlit_app.py

Deploy (free): push this folder to a public GitHub repo, then create an app at
https://share.streamlit.io pointing at streamlit_app.py.
"""

from pathlib import Path
import streamlit as st

st.set_page_config(
    page_title="NHS CHC Decision Support Tool",
    page_icon="🩺",
    layout="centered",
)

# Load the self-contained questionnaire HTML (sits next to this file).
HTML_PATH = Path(__file__).parent / "dst_app.html"

try:
    html = HTML_PATH.read_text(encoding="utf-8")
except FileNotFoundError:
    st.error(
        "Could not find dst_app.html. Make sure it is in the same folder as "
        "streamlit_app.py."
    )
    st.stop()

# Render the questionnaire. Height is generous so long domains don't clip;
# scrolling is enabled for the taller domains and the results page.
st.components.v1.html(html, height=1500, scrolling=True)

# A short footer outside the iframe. Keep the medical/scope caveat visible.
st.caption(
    "This is an unofficial aid based on the July 2022 DST care-domain "
    "descriptors. It is not affiliated with the NHS and does not replace a "
    "statutory assessment or professional advice. Eligibility for NHS "
    "Continuing Healthcare is decided by a multidisciplinary team."
)
