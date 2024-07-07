import os

from autogen import ConversableAgent
from llm_config import llm_config


def init_coding_agents():
    human_proxy = ConversableAgent(
        "human_proxy",
        llm_config=llm_config,
        code_execution_config=False,
        function_map=None,
        human_input_mode="ALWAYS",
    )
    return human_proxy
