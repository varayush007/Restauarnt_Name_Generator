import streamlit as st
import langchain_helper

st.title("Restaurant Name Generator")
cuisine, temperature, location = st.columns([1, 1, 1])

cuisine = cuisine.text_input("Enter a Cuisine", "")
temperature = temperature.text_input("Creative Answers (0.1 to 1.0)", "")
location = location.text_input("Restaurant Location", "")


if cuisine:
    response = langchain_helper.generate_restaurant_name_and_items(cuisine,temperature, location)

    # Display results
    st.header(response['restaurant_name'].strip())
    st.subheader("Menu Items:")
    st.write(response['menu_items'].strip())


