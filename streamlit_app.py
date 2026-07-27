"""The Dark Forest Registry — a spoiler-free character map of Liu Cixin's
Remembrance of Earth's Past trilogy, served through Streamlit.

Streamlit is Python and cannot run JSX directly, so the React component lives
in `app_component.html` (React and Babel load from CDNs, so there is no build
step). This script just reads that file and embeds it.
"""

from pathlib import Path

import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="The Dark Forest Registry",
    page_icon="\U0001F30C",  # 🌌
    layout="wide",
    initial_sidebar_state="collapsed",
)

# Trim Streamlit's default chrome/padding so the registry fills the page.
st.markdown(
    """
    <style>
      header[data-testid="stHeader"] { display: none; }
      .block-container { padding: 0 !important; max-width: 100% !important; }
      [data-testid="stAppViewContainer"] { background: #07080d; }
    </style>
    """,
    unsafe_allow_html=True,
)

html = (Path(__file__).parent / "app_component.html").read_text(encoding="utf-8")

# One screenful tall; the constellation and the dossier scroll within the iframe.
components.html(html, height=900, scrolling=True)
