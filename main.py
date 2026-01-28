from dotenv import load_dotenv
from pydantic import BaseModel
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
import lmstudio as lms


load_dotenv()


api_host = lms.Client.find_default_local_api_host() or "http://127.0.0.1:4000"
lms.configure_default_client(api_host)

model = lms.llm()

chat = lms.Chat("You are a helpful assistant.")  
chat.add_user_message("Hello how are you?")
response = model.respond(chat)
print(response)