from socket_module import socketio,session

def phoneCall(name):

    print(name)

    socketio.emit("call",name,room=session["room"])
    return f"Phone call made to {name}"
    
from typing import Type
from pydantic import BaseModel, Field
from langchain.tools import BaseTool


class phoneCallInput(BaseModel):
    """Inputs for the PhoneCallTool"""

    name: str = Field(description="The name of the the person to be called")


class PhoneCallTool(BaseTool):
    name = "PhoneCallTool"
    description = """
        Useful when you want to make a phone call.
        You should enter the name of the person to make the phone call
        """
    args_schema: Type[BaseModel] =phoneCallInput
    
    def _run(self, name: str):
        phone_response = phoneCall(name)
        return phone_response

    def _arun(self, name: str):
        phone_response = phoneCall(name)
        return phone_response