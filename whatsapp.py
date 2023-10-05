from socket_module import socketio,session

def SendWhatsapp(message,name):

    print(message,name)
    socketio.emit("whatsapp",[message,name],room=session["room"])

    return f"Whatsapp Message Initiated to {name}"
    
from typing import Type
from pydantic import BaseModel, Field
from langchain.tools import BaseTool


class SendWhatsappInput(BaseModel):
    """Inputs for the SendWhatsappTool"""

    name: str = Field(description="The name of the the person to send the Whatsapp message")
    message: str = Field(description="The Whatsapp message content to be sent")


class SendWhatsappTool(BaseTool):
    name = "SendWhatsappTool"
    description = """
        Useful when you want to Send Whatsapp Message.
        You should enter the name of the person to Send Whatsapp Message
        """
    args_schema: Type[BaseModel] = SendWhatsappInput
    
    def _run(self, message: str,name: str):
        message_response = SendWhatsapp(message,name)
        return message_response

    def _arun(self, message: str,name: str):
        message_response = SendWhatsapp(message,name)
        return message_response