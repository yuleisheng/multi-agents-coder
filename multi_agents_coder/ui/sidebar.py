import os
import streamlit as st

from dotenv import load_dotenv

load_dotenv()


def sidebar():
    with st.sidebar:
        st.markdown(
            "## How to use\n"
            "1. Enter your [OpenAI API key](https://platform.openai.com/account/api-keys)\n"
            "2. Ask a coding question\n"
        )
        api_key_input = st.text_input(
            "OpenAI API Key",
            type="password",
            placeholder="Paste your OpenAI API key here",
            help="Get your API key from https://platform.openai.com/account/api-keys",
            value=os.environ.get("OPENAI_API_KEY", None)
            or st.session_state.get("OPENAI_API_KEY", ""),
        )

        st.session_state["OPENAI_API_KEY"] = api_key_input

        st.markdown("---")
        st.markdown("# About")
        st.markdown(
            "A team of agents will help you to write code"
        )
        st.markdown(
            "Made by [yulei](https://www.linkedin.com/in/yulei-sheng-505b7490/)")
