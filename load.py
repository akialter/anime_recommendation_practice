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

@st.cache
def load_cloud(fs, bucket_path, file_name):
    with fs.open(bucket_path + file_name) as f:
        content = pandas.read_pickle(f)
    return content

bucket_path = 'anime_recommendation_dataset_practice/'
project_name = 'My First Project'

# interface with Google Cloud Storage using gcsfs
fs = gcsfs.GCSFileSystem(project = project_name, token = 'anon')
anime_name_search = load_cloud(fs, bucket_path, 'anime_name_search_2022.pickle')    
