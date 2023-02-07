# -*- coding: utf-8 -*-
"""
Created on Mon Feb  6 20:21:49 2023

@author: Phat Bui
"""

import streamlit as st
from api_request import get_anime
import os
import base64

def anime_list_in_col(pics, urls, names):
    col1, col2, col3, col4 = st.columns(4, gap="large")
    with col1:
        st.caption(names[0])
        if pics[0] == "Error":
            st.text = "Error"
        else:
            html_code = f'''
                <a href="{urls[0]}">
                    <img src="{pics[0]}" style="width:158px;height:221px:" />
                </a>'''
            st.markdown(html_code, unsafe_allow_html=True)
    with col2:
        st.caption(names[1])
        if pics[1] == "Error":
            st.text = "Error"
        else:
            html_code = f'''
                <a href="{urls[1]}">
                    <img src="{pics[1]}" style="width:158px;height:221px:" />
                </a>'''
            st.markdown(html_code, unsafe_allow_html=True)
    with col3:
        st.caption(names[2])
        if pics[2] == "Error":
            st.text = "Error"
        else:
            html_code = f'''
                <a href="{urls[2]}">
                    <img src="{pics[2]}" style="width:158px;height:221px:" />
                </a>'''
            st.markdown(html_code, unsafe_allow_html=True)
    with col4:
        st.caption(names[3])
        if pics[3] == "Error":
            st.text = "Error"
        else:
            html_code = f'''
                <a href="{urls[3]}">
                    <img src="{pics[3]}" style="width:158px;height:221px:" />
                </a>'''
            st.markdown(html_code, unsafe_allow_html=True)
    # separate spacer
    st.text(" ")
    st.text(" ")
    st.text(" ")
    
def single_anime(pic, url):
    html_code = f'''
                <a href="{url}">
                    <img src="{pic}" style="width:158px;height:221px:" />
                </a>'''
    st.markdown(html_code, unsafe_allow_html=True)
        