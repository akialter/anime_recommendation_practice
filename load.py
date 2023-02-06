# -*- coding: utf-8 -*-
"""
Created on Sun Feb  5 19:57:29 2023

@author: Phat Bui
"""

import pandas 
import pickle
import gcsfs
import streamlit as st
from google.oauth2 import service_account
from google.cloud import storage

# create API client.
credentials = service_account.Credentials.from_service_account_info(
    st.secrets["gcp_service_account"]
)
client = storage.Client(credentials=credentials)

# interface with Google Cloud Storage using gcsfs
fs = gcsfs.GCSFileSystem(project = 'My First Project', token = 'anon')
with fs.open('anime_recommendation_dataset_practice/anime_df.pickle') as f:
    anime_df = pandas.read_pickle(f)

with fs.open('anime_recommendation_dataset_practice/anime_name_search.pickle') as f:
    anime_name_search = pandas.read_pickle(f)
    
with fs.open('anime_recommendation_dataset_practice/anime_trained_model.sav', 'rb') as f:
    anime_model = pickle.load(f)

