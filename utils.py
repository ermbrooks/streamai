import os, boto3

def get_session():
    acces_key = os.environ["Access"]
    secret_key = os.environ["Secret"]
    session_token = os.environ["Session"]
    return boto3.Session(acces_key, secret_key, session_token, region_name="us-east-1")

def get_cognito_info():
    app_client = os.environ["UserPool"]
    app_id = os.environ["AppClient"]
    app_secret = os.environ["AppSecret"]
    cognito_domain = os.environ["CognitoDomain"]
    return (app_client, app_id, app_secret, cognito_domain)

def list_available_models():
    session = get_session()
    bedrock = session.client("bedrock")
    models = bedrock.list_foundation_models()
    return models

def execute_prompt(prompt, model):
    session = get_session()
    bedrock_runtime = session.client("bedrock_runtime")