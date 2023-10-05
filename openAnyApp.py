from socket_module import socketio,session


def openApp(app):
    print(session["room"])
    socketio.emit("openapp",app,room=session["room"])  
    return f"{app} is opened now"
    
from typing import Type
from pydantic import BaseModel, Field
from langchain.tools import BaseTool


class OpenAppInput(BaseModel):
    """Inputs for the OpenAppTool"""

    app: str = Field(description="The name of the app that needs to be opened the first letter of the app should be in lowercase")


class OpenAppTool(BaseTool):
    name = "OpenAppTool"
    description = """
        Useful when you want to open any apps.
        You should enter the app name to open the app and the first letter of the app should be in lowercase
        """
    args_schema: Type[BaseModel] = OpenAppInput
    
    def _run(self, app: str):
        app_response = openApp(app)
        return app_response

    def _arun(self, app: str):
        app_response = openApp(app)
        return app_response