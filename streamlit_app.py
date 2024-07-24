import streamlit as st
import utils
from streamlit_cognito_auth import CognitoHostedUIAuthenticator

(client, id, secret) = utils.get_cognito_info()
authenticator = CognitoHostedUIAuthenticator(client, id, secret, use_cookies=False)

is_logged_in = authenticator.login()
if not is_logged_in:
    print("Login failed")

st.write(utils.list_available_models())