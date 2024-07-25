import boto3, utils
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_community.chat_models import BedrockChat


class BedrockClient():
    def __init__(self) -> None:
        session = utils.get_session()
        self.bedrock_runtime = session.client(
            service_name="bedrock-runtime",
            region_name="us-east-1"
        )
        self.model_id = "anthropic.claude-3-sonnet-20240229-v1:0"
        self.model_kwargs = {
            "max_tokens": 2048,
            "temperature": 0.0,
            "top_k": 250,
            "top_p": 1,
            "stop_sequences": ["\n\nHuman"],
        }
        self.model = self.setup_model()

    def __setup_model(self):
        return BedrockChat(
            client=self.bedrock_runtime,
            model_id=self.model_id,
            model_kwargs=self.model_kwargs,
        )
    
    def execute_prompt(prompt_text):
        pass