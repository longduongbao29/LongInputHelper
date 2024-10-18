
from langchain_core.prompts import ChatPromptTemplate


SUMMARY_TEMPLATE = """
You are a helpful assistant that sumarize document. Summarize the document no more than 1024 tokens.
Just return only summary content, not any instruction sentences such as 'Here is the summary'.

Previous paragraph summary:
{previous}

Summerize following document:{input}

Output (document summary):
"""
summarize_prompt = ChatPromptTemplate.from_template(SUMMARY_TEMPLATE, vars = ['previous', 'input'])

CORRECT_SPELLING_TEMPLATE = """
You are a helpful assistant that corrects spelling and grammar mistakes.
Just return pairs for each including 2 sentences: incorrect and its corrected version, seperated by '|'
For each pair, return whole sentences.
Do not return pairs that no change needed.
Do not return instruction sentences such as 'Here are the corrected pairs:'

EXAMPLE 1:
Previous paragraph summary:
The document is introduced about the author himself.

Input:
I am a doctoh. My name is David. I are 40 years old.

Output:
("I am a doctoh"=>"I am a doctor")|("I are 40 years old"=>"I am 40 years old")
END OF EXAMPLE


EXAMPLE 2:
Previous paragraph summary:
The document is introduced about the author himself.

Input:
I lived with my parents when i was a child. My mother said: "Your shouldd been kind to everyone".

Output:
("My mother said: "Your shouldd been kind to everyone""=>"My mother said: "Your should be kind to everyone"")

END OF EXAMPLE

Begin
Previous paragraph summary:
{previous}

Input:
{input}

Output (pairs):"""

correct_spelling_prompt = ChatPromptTemplate.from_template(CORRECT_SPELLING_TEMPLATE, vars =['input', 'previous'])