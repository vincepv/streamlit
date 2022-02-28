import streamlit as st

from component.header import header
from component.clean_file import clean_file
from component.api_name import get_age
from component.graph import graph

header()
graph()
clean_file()
get_age()





