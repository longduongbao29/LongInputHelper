import getpass
import os  
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from prompts import summarize_prompt
if "GROQ_API_KEY" not in os.environ:
    os.environ["GROQ_API_KEY"] = getpass.getpass("Enter your Groq API key: ")
llm = ChatGroq(
    model="llama3-8b-8192",
    temperature=0,
    max_tokens=None,
    timeout=None,
    max_retries=2,
    # other params...
)
summarize_llm = llm = ChatGroq(
    model="llama3-8b-8192",
    temperature=0,
    max_tokens=None,
    timeout=None,
    max_retries=2,
    # other params...
)

async def call(prompt : ChatPromptTemplate,input: str):
    chain = prompt | llm
    output = await chain.ainvoke(input)
    return output

async def summrize_call(input: str):
    chain = summarize_prompt | summarize_llm 
    output = await chain.ainvoke(input)
    return output