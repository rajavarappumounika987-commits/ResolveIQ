import streamlit as st


def apply_styles():
    st.markdown(
        """
        <style>

        .main-title {
            font-size: 40px;
            font-weight: 700;
        }

        .subtitle {
            font-size: 20px;
        }

        </style>
        """,
        unsafe_allow_html=True
    )
