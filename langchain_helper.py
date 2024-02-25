from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain, SequentialChain

import os
from dotenv import load_dotenv
load_dotenv()


def generate_restaurant_name_and_items(cuisine, temperature=None, location=None, restaurant_name=None):
    # Initialize the OpenAI language model with user-defined temperature
    llm = OpenAI(api_key=os.getenv("openapi_key"), temperature=temperature)

    # Chain 1: Restaurant Name
    prompt_template_name = PromptTemplate(
        input_variables=['cuisine'],
        template=f"I want to open a restaurant with {cuisine} cuisine{' in ' + location if location else ''}. Suggest a fancy name for it."
    )
    name_chain = LLMChain(llm=llm, prompt=prompt_template_name, output_key="restaurant_name")

    # Chain 2: Menu Items
    prompt_template_items = PromptTemplate(
        input_variables=['restaurant_name'],
        template=f"Suggest the names of 10 menu items for {restaurant_name}."
    )
    food_items_chain = LLMChain(llm=llm, prompt=prompt_template_items, output_key="menu_items")

    # Sequential Chain combining both chains
    chain = SequentialChain(
        chains=[name_chain, food_items_chain],
        input_variables=['cuisine'],
        output_variables=['restaurant_name', 'menu_items']
    )

    # Generate response
    response = chain({'cuisine': cuisine})
    return response

if __name__ == "__main__":
     print(generate_restaurant_name_and_items("Indian",1))


