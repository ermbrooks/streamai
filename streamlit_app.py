import streamlit as st
import utils
from streamlit_cognito_auth import CognitoHostedUIAuthenticator
import authenticate

# (client, id, secret, uri) = utils.get_cognito_info()
# authenticator = CognitoHostedUIAuthenticator(client, id, secret, use_cookies=False)

# is_logged_in = authenticator.login()
# if not is_logged_in:
#     print("Login failed")

# st.write(utils.list_available_models())

# Check authentication when user lands on the home page.
authenticate.set_st_state_vars()

# Add login/logout buttons
if st.session_state["authenticated"]:
    authenticate.button_logout()
else:
    authenticate.button_login()