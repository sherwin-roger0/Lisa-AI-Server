

from langchain.tools.python.tool import PythonREPLTool
from langchain.memory import ConversationBufferMemory
from langchain.chat_models import ChatOpenAI
from langchain.agents import initialize_agent
from langchain.agents import AgentType
from langchain.prompts import MessagesPlaceholder
from langchain.memory import ConversationBufferMemory
from langchain.tools import Tool
from langchain.tools import DuckDuckGoSearchRun
from spot import SpotifyTool
from openAnyApp import OpenAppTool
from phoneCall import PhoneCallTool
import os
from reminder import send_reminderTool
import os
import pprint
from langchain.utilities.google_serper import GoogleSerperAPIWrapper

search_places = GoogleSerperAPIWrapper(type="places",serper_api_key="a6f1b5531fb1c676d71351089471cdb510f2b204",gl="in")

search_places = Tool(
        name = "search_places",
        func=search_places.results,
        description="useful when u want to find a particular place or exact location of that place and the details of that place"
)


os.environ["OPENAI_API_KEY"] = "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"

search = DuckDuckGoSearchRun()

search_tool = Tool(
        name = "search",
        func=search.run,
        description="useful for when you need to answer questions about current events"
)

llm = ChatOpenAI(temperature=0, model="gpt-3.5-turbo-0613")
memory = ConversationBufferMemory(memory_key="memory", return_messages=True)


print(memory.load_memory_variables({}))


self_ask_with_search = initialize_agent([SpotifyTool(),PythonREPLTool(),search_tool,OpenAppTool(),PhoneCallTool(),send_reminderTool(),search_places], llm,
            agent=AgentType.OPENAI_FUNCTIONS, memory=memory, agent_kwargs={
                "extra_prompt_messages": [MessagesPlaceholder(variable_name="memory")],
            }, verbose=True)
    
    
self_ask_with_search.run("restaurant near Zone 8 Anna Nagar ,Chennai,'Chennai District','Tamil Nadu','600001','India'")