from gevent import monkey
monkey.patch_all()
from flask import Flask,request
from flask_cors import CORS
from socket_module import socketio,session

app = Flask(__name__)
socketio.init_app(app, cors_allowed_origins="*")
CORS(app)

from langchain.tools.python.tool import PythonREPLTool
from langchain.memory import ConversationBufferMemory
from langchain.chat_models import ChatOpenAI
from langchain.agents import initialize_agent
from langchain.agents import AgentType
from langchain.prompts import MessagesPlaceholder
from langchain.schema import SystemMessage
from langchain.memory import ConversationBufferMemory
from langchain.memory import MongoDBChatMessageHistory
from langchain.tools import Tool
from langchain.tools import DuckDuckGoSearchRun
from spot import SpotifyTool
from openAnyApp import OpenAppTool
from phoneCall import PhoneCallTool
import os
from sendEmail import emailTool
from reminder import send_reminderTool
from sendMessage import SendMessageTool
from create_image import GetImageTool
from maps import mapsTool
from whatsapp import SendWhatsappTool

os.environ["OPENAI_API_KEY"] = "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"

search = DuckDuckGoSearchRun()

search_tool = Tool(
        name = "search",
        func=search.run,
        description="useful for when you need to answer questions about current events"
)

llm = ChatOpenAI(temperature=0, model="gpt-3.5-turbo-0613")
uri = "mongodb+srv://sherwinroger:tronster@cluster0.vvp2vpz.mongodb.net/?retryWrites=true&w=majority"
    
@socketio.on('question')
def handle_request_update(data):
    print("q",session["room"])
    
    message_history = MongoDBChatMessageHistory(
        connection_string=uri, session_id=session["room"]
    )
    memory = ConversationBufferMemory(memory_key="memory", return_messages=True,chat_memory=message_history)
    
    self_ask_with_search = initialize_agent([SpotifyTool(),PythonREPLTool(),search_tool,OpenAppTool(),PhoneCallTool(),send_reminderTool(),emailTool(),SendMessageTool(),GetImageTool(),mapsTool(),SendWhatsappTool()], llm,
                agent=AgentType.OPENAI_FUNCTIONS, memory=memory, agent_kwargs={
                    "system_message": SystemMessage(content="Your are an Highly intelligent AI which is present inside an app named as Lisa AI,your name is Lisa, You got your name from a kpop group named blackpink member Lisa Manoban,Your job is to do everything that your user asks you to do, You should do everything that your user asks you to do using the given tools, even if the user asks you to do a task multiple times you should do it you shold never say i have already done that task and your creator name is Sherwin Roger who is a Google certified Tensorflow developer and he can create web apps and mobile apps too."),
                    "extra_prompt_messages": [MessagesPlaceholder(variable_name="memory")]
                }, verbose=True)
    socketio.emit('answer', [data[0],self_ask_with_search.run(data[0]["text"]),data[1]],room=session["room"])
    
    
if __name__ == '__main__':
    app.run(debug=True)