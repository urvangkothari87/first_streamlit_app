import streamlit as s
import pandas

s.title('My familys New Healthy Diner')

s.header('Breakfast Menu')
s.text('Omega 3 & Blueberry Oatmeal')
s.text('Banana, Mango, and Spinach Smoothie')
s.text('Hard-Boiled Free-Range Eggs')
s.text('Avocado Toast')

s.header('Build Your Own Fruit Smoothie')

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

# Let's put a pick list here so customers can pick the fruit they want to include
fruits_selected = s.multiselect("Pick some fruits:", list(my_fruit_list.index), ['Avocado', 'Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]

# Display the table on the page
s.dataframe(fruits_to_show)


