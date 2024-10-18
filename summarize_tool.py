from prompts import summarize_prompt
from limit_input_helper import recursive
from doc  import doc
from limit_input_helper import num_tokens_from_string
from langchain.tools import tool
import asyncio

# Brute Force Chunk | RAG https://js.langchain.com/v0.2/docs/how_to/extraction_long_text/


# @tool
async def recursive_summarize(text):
    """This tool use for summarizing a document. Use this tool for sumarizing tasks."""
    output = await recursive(text, summarize_prompt)
    return output
# print("Num tokens: ",num_tokens_from_string(doc))
async def main():
    import time
    start_time = time.time()
    summerize = await asyncio.create_task(recursive_summarize(doc))
    end_time = time.time()
    print("Summerized: ",summerize)
    print("Time:", (end_time-start_time))
    print("Num document tokens: ",num_tokens_from_string(doc))
    print("Num summary tokens: ",num_tokens_from_string(summerize))

if __name__ == '__main__': 
    asyncio.run(main())