from limit_input_helper import recursive
from prompts import correct_spelling_prompt
from doc import incorrect_spelling_doc
from limit_input_helper import num_tokens_from_string
import asyncio
import re

def str2tuple(string:str):
    components = string.strip("()").split("=>")
    components = [c.replace("\"",'') for c in components]

    return components
async def correct_spelling(text):
    pairs = await recursive(text, prompt= correct_spelling_prompt)
    pairs = re.split(r'(\|)|(\n)', pairs)
    pairs = [pair for pair in pairs if (pair not in ["|","\n"] and pair)]
    pairs = [str2tuple(pair) for pair in pairs]
    modified_text:str = text
    for pair in pairs:
        if len(pair) == 2:
            modified_text = modified_text.replace(pair[0], pair[1])
    return modified_text
async def main():
    import time
    start_time = time.time()
    modified_doc = await asyncio.create_task(correct_spelling(incorrect_spelling_doc))
    end_time = time.time()
    print("Correct spelling and grammar ",modified_doc)
    print("Num document tokens: ",num_tokens_from_string(incorrect_spelling_doc))
    print("Time:", (end_time-start_time))

if __name__ == '__main__': 
    asyncio.run(main())