import boto3, utils
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_community.chat_models import BedrockChat
import logging
from logging import getLogger

class BedrockClient():
    def __init__(self) -> None:
        
        self.logger = getLogger()
        self.logger.addHandler(logging.StreamHandler())
        self.logger.setLevel(logging.INFO)

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
        self.system_message = "You are a helpful assistant."
        self.user_messages = []

    def __setup_model(self):
        return BedrockChat(
            client=self.bedrock_runtime,
            model_id=self.model_id,
            model_kwargs=self.model_kwargs,
        )
    
    def execute_prompt(self, prompt_text):
        self.user_messages.append(prompt_text)
        prompt = ChatPromptTemplate.from_messages([("system", self.system_message), ("user", {prompt_text})])
        chain = prompt | self.model | StrOutputParser()
        try:
            return chain.invoke({"prompt_text": prompt_text})
        except:
            self.logger.info(f"prompt {prompt_text} execution failed")
        