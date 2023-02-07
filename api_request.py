# -*- coding: utf-8 -*-
"""
Created on Mon Feb  6 18:27:53 2023

@author: Phat Bui
"""

import requests
import json
import time

get_api = "https://api.jikan.moe/v4/"
  
def batch_request(anime_list):
    pics, urls, names = [], [], []
    for a in anime_list:
        p, u, n = get_anime(a)
        pics.append(p)
        urls.append(u)
        names.append(n)
    return (pics, urls, names)

# get the image url, mal url and name of the anime given 
def get_anime(anime_id):
    params = "anime/" + str(anime_id)
    response = requests.get(get_api + params)
    
    time.sleep(0.4) # to avoid too fast API call
    if response.status_code == 200:
        data = json.loads(response.text)
        pic = data['data']['images']['webp']['image_url']
        url = data['data']['url']
        name = data['data']['title']
        return (pic, url, name)
    else:
        return ("Error", "Error", "Error")
    
# search for the anime by the first letters based on the search key
def search_anime(search_key):
    response = requests.get(get_api + 'anime', params={'letter': search_key})

    if response.status_code == 200:
        data = json.loads(response.text)
        query_list = []
        for cur in data['data']:
            # search result is a tuple of (pic_url, mal_url, name, id)
            query_list.append((cur['images']['webp']['image_url'], cur['url'], cur['title'], cur['mal_id']))
        
        return query_list
    else:
        return []
    
# return a list of recommended animes based on the anime id input
def recommend_anime(anime_id):
    response = requests.get(get_api + 'anime/' + str(anime_id) + '/recommendations')
    query_list = []

    time.sleep(0.4) # to avoid too fast API call
    if response.status_code == 200:
        data = json.loads(response.text)
        for cur in data['data']:
            # append all id of recommended animes in a list
            query_list.append(cur['entry']['mal_id'])
        
        return query_list
    else:
        return []
        