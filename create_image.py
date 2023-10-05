from serpapi import GoogleSearch
from socket_module import socketio,session

def GetImage(image):
    params = {
    "q": image,
    "engine": "google_images",
    "ijn": "0",
    "api_key": "43dbe31f48ad3f10e607dba805bd5b4fb3f4aa752c1ad692a3c1c4f74b99cbff"
    }

    search = GoogleSearch(params)
    results = search.get_dict()
    print(results)
    images_results = results["images_results"]
    print(images_results[0]["thumbnail"])

    socketio.emit("image-message",images_results[0]["thumbnail"],room=session["room"])

    return f"This is the image link {images_results[0]['thumbnail']}"
    
from typing import Type
from pydantic import BaseModel, Field
from langchain.tools import BaseTool


class GetImageInput(BaseModel):
    """Inputs for the GetImageTool"""

    image_name: str = Field(description="The name of the image")


class GetImageTool(BaseTool):
    name = "GetImageTool"
    description = """
        Useful when you want to get an image.
        You should enter the name of the image to get the image
        """
    args_schema: Type[BaseModel] = GetImageInput
    
    def _run(self, image_name: str):
        image_response = GetImage(image_name)
        return image_response

    def _arun(self, image_name: str):
        image_response = GetImage(image_name)
        return image_response