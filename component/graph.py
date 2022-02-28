import streamlit as st
import graphviz as graphviz 

def graph():
    # Create a graphlib graph object
    st.header("Premières questions avant le début de l'étude")
    graph = graphviz.Digraph()
    graph.edge('base client', 'qui sont les clients ?')
    graph.edge('base client', 'quel est la récurrence ?')
    graph.edge('base client', 'quels sont les articles ?')
    graph.edge('base client', 'quel est le panier moyen ?')

    graph.edge('qui sont les clients ?','Majorité de femme')


    st.graphviz_chart(graph)

