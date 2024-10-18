from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from call_chat_api import llm
from limit_input_helper import num_tokens_from_string
from summarize_tool import recursive_summarize
prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "You are very powerful assistant",
        ),
        ("user", "{input}"),
        MessagesPlaceholder(variable_name="agent_scratchpad"),
    ]
)   
tools =[recursive_summarize]
llm_with_tools = llm.bind_tools(tools)