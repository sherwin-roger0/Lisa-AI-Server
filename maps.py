
def maps(location):

    return f"link for {location} is https://www.google.com/maps/search/?api=1&query={location}"
    
from typing import Type
from pydantic import BaseModel, Field
from langchain.tools import BaseTool


class mapsInput(BaseModel):
    """Inputs for the mapsTool"""

    location: str = Field(description="The name of the location that needs to be opened in the map")


class mapsTool(BaseTool):
    name = "mapsTool"
    description = """
        Useful when you want to open any location in maps.
        You can find any places using this tool
        """
    args_schema: Type[BaseModel] = mapsInput
    
    def _run(self, location: str):
        maps_response = maps(location)
        return maps_response

    def _arun(self, location: str):
        maps_response = maps(location)
        return maps_response