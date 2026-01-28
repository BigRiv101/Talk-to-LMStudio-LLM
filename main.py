from dotenv import load_dotenv
from pydantic import BaseModel
import lmstudio as lms
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import PydanticOutputParser

load_dotenv()

class ResearchResponse(BaseModel):
    topics: str
    summary: str
    sources: list[str]
    tools_used: list[str]




api_host = lms.Client.find_default_local_api_host() or "http://127.0.0.1:4000"
lms.configure_default_client(api_host)
model = lms.llm()

parser = PydanticOutputParser(pydantic_object=ResearchResponse)

prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """
            You are a research assistant that will help generate a research paper.
            Answer the user query and use necessary tools. 
            Wrap the output in this format and provide no other text\n{format_instructions}
            """,
        ),
        ("placeholder", "{chat_history}"),
        ("human", "{query}"),
        ("placeholder", "{agent_scratchpad}"),
    ]
).partial(format_instructions=parser.get_format_instructions())