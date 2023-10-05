from socket_module import socketio,session

def SendMessage(message,name):

    print(message,name)
    socketio.emit("message",[message,name],room=session["room"])

    return f"Message Initiated to {name}"
    
from typing import Type
from pydantic import BaseModel, Field
from langchain.tools import BaseTool


class SendMessageInput(BaseModel):
    """Inputs for the SendMessageTool"""

    name: str = Field(description="The name of the the person to send the message")
    message: str = Field(description="The message content to be sent")


class SendMessageTool(BaseTool):
    name = "SendMessageTool"
    description = """
        Useful when you want to Send Message.
        You should enter the name of the person to Send Message
        """
    args_schema: Type[BaseModel] = SendMessageInput
    
    def _run(self, message: str,name: str):
        message_response = SendMessage(message,name)
        return message_response

    def _arun(self, message: str,name: str):
        message_response = SendMessage(message,name)
        return message_response