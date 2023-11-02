import os
from langchain.prompts import PromptTemplate
from langchain.llms import OpenAI

os.environ["OPENAI_API_KEY"] = "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"

def generate_description(input):
    llm = OpenAI(temperature=0.9)
    prompt = PromptTemplate(
        input_variables=["input"],
        template="As a Product Description Generator, Generator multi paragraph rich text product description with emojis from the {input}?",
    )

    from langchain.chains import LLMChain
    chain = LLMChain(llm=llm, prompt=prompt)

    result = chain.run(input)
    return result