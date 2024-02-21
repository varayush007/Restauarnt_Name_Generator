# Restaurant Name and Menu Generator

This Streamlit app generates a restaurant name and sample menu items based on a selected cuisine type, temperature and location. It utilizes the LangChain library to construct a chain of OpenAI models to first generate a restaurant name based on the cuisine and then generate menu items fitting that restaurant name.

## Overview

The app uses the LangChain library to create a pipeline for generating the restaurant name and menu items using OpenAI. It constructs a SequentialChain combining two LLMChains.

## Code Overview

- `langchain_helper.py`: Defines the LangChain pipeline for generating the restaurant name and menu items using OpenAI. It constructs a SequentialChain combining two LLMChains.

- `main.py`: Streamlit app that provides the user interface and calls the LangChain pipeline. It displays the generated outputs.

## Running the App

1. Install requirements:

    ```
    pip install -r requirements.txt
    ```

2. Add your OpenAI API key to `secret_key.py`.

3. Run the app:

    ```
    streamlit run main.py
    ```

## Usage

1. Select a cuisine type
2. Set the OpenAI temperature (0.1-1.0) to control randomness
3. Specify a location to incorporate into the name
4. View generated name and menu items

## Requirements

- Python 3.x
- Streamlit
- LangChain
- OpenAI API key
![Screenshot](Screenshot(89).png)

