import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from socket_module import socketio,session

# Set up the Spotify API credentials
client_id = 'bf44a86d301046cbb4149e221791d18a'
client_secret = '74cbbfde60e04493a1173bc97ab533dc'

# Create the Spotipy client with client credentials flow
auth_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(auth_manager=auth_manager)

# Prompt the user to enter the song name
def spotify(song):

    print(song)
    results = sp.search(q=song, type='track', limit=1)

    # Extract the relevant information from the search results
    if results['tracks']['total'] > 0:
        track = results['tracks']['items'][0]
        socketio.emit("spotify",track['id'],room=session["room"])
        return "Song is playing now"
    
from typing import Type
from pydantic import BaseModel, Field
from langchain.tools import BaseTool


class SpotifyInput(BaseModel):
    """Inputs for the Spotify song Tool"""

    song: str = Field(description="The name of the song")


class SpotifyTool(BaseTool):
    name = "SpotifyTool"
    description = """
        Useful when you want to play a song.
        You should enter the song name to play the song
        """
    args_schema: Type[BaseModel] = SpotifyInput
    
    def _run(self, song: str):
        spotify_response = spotify(song)
        return spotify_response

    def _arun(self, song: str):
        spotify_response = spotify(song)
        return spotify_response