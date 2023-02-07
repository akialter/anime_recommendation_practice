# -*- coding: utf-8 -*-
"""
Created on Tue Feb  7 01:10:13 2023

@author: Phat Bui
"""

from api_request import batch_request, get_anime, search_anime, recommend_anime
from get_format import anime_list_in_col, single_anime
from load import anime_name_search
from fuzzywuzzy import fuzz
from fuzzywuzzy import process
import streamlit as st
import re

# clean a name (remove non-alphabetic char and space)
def clean_name(name):
    name = re.sub("[^a-zA-Z0-9]", "", name)
    return name.lower()

# return the MAL id the searched anime name
def search(name):
    name = clean_name(name)
    result = process.extractOne(name, anime_name_search['Title'].apply(clean_name))
    result_eng = process.extractOne(name, anime_name_search['English'].replace("Unknown", "").apply(clean_name))
    if result[1] <= 80 and result[2] <= 80:
        return 0
    else:
        return anime_name_search._get_value(result[2], 'ID') if result_eng[1] <= result[1] else anime_name_search._get_value(result_eng[2], 'ID')


def wait_while_request(anime_list):
    with st.spinner('Fetching...'):
        return batch_request(anime_list)
    
def wait_while_recommend(anime_id):
    with st.spinner('Recommending...'):
        return recommend_anime(anime_id)
    
def wait_while_search(anime_id):
    with st.spinner('Searching...'):
        return get_anime(anime_id)

def main():
    st.title('Anime Recommnendation Web App')
    anime_name = st.text_input('Input anime name')
    
    if st.button('Get recommendation'):
        # get the id of the anime based on user's input
        anime_id = search(anime_name)
           
        if anime_name == "":
            st.error('No input', icon='❗')
        elif not anime_id:
            st.error('Anime not found', icon='❗')
        else:
            pic, url, name = wait_while_search(anime_id)
            single_anime(pic, url)
            st.subheader('Recommendation for: ' + name)
            
            # recommend animes based on the id, only take first 8 entries of the recommendation
            anime_list = wait_while_recommend(anime_id)
            
            if not anime_list:
                st.error('Sorry. Could not find any recommendation for this anime.')
            else:
                # fetch each 4 due to time limit of api calls (avoid long waiting)
                pics, urls, names = wait_while_request(anime_list[0:4])
                anime_list_in_col(pics, urls, names)
                
                # fetch each 4 due to time limit of api calls (avoid long waiting)
                pics, urls, names = wait_while_request(anime_list[4:8])
                anime_list_in_col(pics, urls, names)

        
if __name__ == '__main__':
    main()
