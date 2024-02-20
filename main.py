import streamlit as st
import langchain_helper

st.header("Restaurant Name and Cuisine Generator")
cuisine = st.sidebar.selectbox("Pick a Cuisine",("Indian","American","Italian","Japanese","Korean","Australian","Arabian","Mexican"))



if cuisine:
    response = langchain_helper.generate_restaurant_name_and_items(cuisine)

    st.subheader(response['restaurant_name'].strip())
    menu_items = response['menu_items'].strip().split(",")
    st.write("**Menu Items**")

    for item in menu_items:
        st.write("-",item)

