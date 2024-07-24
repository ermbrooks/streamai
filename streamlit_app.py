import streamlit as st
import os, boto3

def get_session():
    acces_key = os.environ["Access"]
    secret_key = os.environ["Secret"]
    session_token = os.environ["Token"]
    return boto3.Session(acces_key, secret_key, session_token)
    

def list_available_models():
    session = get_session()
    bedrock = session.client("bedrock")
    models = bedrock.list_foundation_models()
    return models



st.write(list_available_models())