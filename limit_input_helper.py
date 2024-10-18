import tiktoken
from langchain_text_splitters import CharacterTextSplitter
from call_chat_api import call, summrize_call
from constant import CHUNK_OVERLAP, INPUT_LIMIT_TOKEN
import asyncio
from langchain_core.prompts import ChatPromptTemplate

def num_tokens_from_string(string: str, encoding_name: str = "o200k_base") -> int:
    """Returns the number of tokens in a text string."""
    encoding = tiktoken.get_encoding(encoding_name)
    num_tokens = len(encoding.encode(string))
    return num_tokens
 
def chunking(doc,chunk_size):
    text_splitter = CharacterTextSplitter(
    separator="\n\n",
    chunk_size=chunk_size,
    chunk_overlap=CHUNK_OVERLAP,
    length_function=num_tokens_from_string,
    is_separator_regex=False,
)

    # num_tokens = num_tokens_from_string(doc)
    chunks = text_splitter.split_text(doc)
    return chunks
async def call_in_parallel(prompt,previous_summarized,chunk):
    out_, previous_summarized_ = await asyncio.gather(
        call(prompt,{'previous':previous_summarized,'input':chunk}),
        summrize_call({'previous':previous_summarized,'input':chunk}),
        return_exceptions=True,
    )
    return out_, previous_summarized_
async def recursive(text:str, prompt:ChatPromptTemplate) -> str:
    """Summarize tool, use this tool for summarize tasks."""
    chunk_size = INPUT_LIMIT_TOKEN - num_tokens_from_string(prompt.messages[0].prompt.template) - 1024
    print("chunk_size: ",chunk_size)
    chunks = chunking(text, chunk_size)
    print("num_chunks: ",len(chunks))
    i= 0
    previous_summarized = ''
    output = ''
    for i in range(0, len(chunks)):
            out_, previous_summarized = await call_in_parallel(prompt,previous_summarized,chunks[i])
            previous_summarized = previous_summarized.content
            output += out_.content + '\n'
            i+=1
            print(f"Summarizing chunk {i}")
    return output