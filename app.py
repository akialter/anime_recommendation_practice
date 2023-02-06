# -*- coding: utf-8 -*-
"""
Created on Sun Feb  5 19:41:35 2023

@author: Phat Bui
"""

import numpy as np
import pandas as pd
import pickle
import re
import streamlit as st
from fuzzywuzzy import fuzz
from fuzzywuzzy import process
from load import anime_model, anime_df, anime_name_search


# a function that takes an anime and return similar animes using the trained model
def predict(anime_name):
    # clean a name (remove non-alphabetic char and space)
    def clean_name(name):
        name = re.sub("[^a-zA-Z0-9]", "", name)
        return name.lower()
    
    # return the official Japanese name of the searched anime name
    def search(name):
        name = clean_name(name)
        result = process.extractOne(name, anime_name_search['Name'].apply(clean_name))
        result_eng = process.extractOne(name, anime_name_search['English name'].replace("Unknown", "").apply(clean_name))
        if result[1] <= 80 and result[2] <= 80:
            return "Anime not found!"
        else:
            return anime_name_search._get_value(result[2], 'Name') if result_eng[1] <= result[1] else anime_name_search._get_value(result_eng[2], 'Name')
    
    query_name = search(anime_name)
    if query_name == "Anime not found!": return "Anime not found!"
    df_index = anime_df.index.get_loc(query_name)
    query = anime_df.iloc[df_index, :].values.reshape(1, -1)
    distance, suggestions = anime_model.kneighbors(query, n_neighbors=11)
    
    recommendation = ""
    for i in range(0, len(distance.flatten())):
        if i == 0:
            recommendation += 'Recommendations for {0}:\n'.format(anime_df.index[df_index])
        else:
            recommendation += '{0}: {1}\n'.format(i, anime_df.index[suggestions.flatten()[i]])
    return recommendation

def main():
    st.title('Anime Recommnendation Web App')
    anime_name = st.text_input('Anime name')
    
    result = ''
    if st.button('Get recommendation'):
        result = predict(anime_name)
    
    st.text(result)
    
if __name__ == '__main__':
    main()