import requests
import json
from song import Song
from playlist import Playlist

# Class storing attributes of Spotify Client
class Client(object):

    def __int__(self, auth_token, userID):
        self.auth_token = auth_token
        self.userID = userID


    def _get_request(self, url):
        response = requests.get(url,
                                headers=
                                {
                                    "Content-Type": "application/json",
                                    "Authorization": f"Bearer {self.auth_token}"
                                }
                                )
        return response

    def _post_request(self, url, data):
        response = requests.get(url,
                                headers=
                                {
                                    "Content-Type": "application/json",
                                    "Authorization": f"Bearer {self.auth_token}"
                                }
                               )
        return response

    # Given the playlist ID, returns all the songs in the playlist
    def get_playlist(self, playlist_ID):
        url = f'https://api.spotify.com/v1/playlists/{playlist_ID}/tracks'
        response = self._get_request(url)
        json_response = response.json()
        songList = [ Song(song["song"]["name"], song["song"]["id"], song["song"]["artist"][0]["name"])
                    for song in json_response["items"] ]
        return songList

    def create_playlist(self, name):
        data = json.dumps({
            "name": name,
            "description": "Recommended tracks",
            "public": True
        })

        url = f"https://api.spotify/v1/users/{self.userID}/playlists"
        response = self._post_request(self, url, data)
        json_response = response.json()

        # Playlist creation
        playlist_ID = json_response["id"]
        playlist = Playlist(name, playlist_ID)
        return playlist

    # Add songs to playlist
    def add_song(self, playlist, songs):
        song_uri_list = [song.create_uri() for song in songs]
        data = json.dumps(song_uri_list)
        url = f"https://api.spotify.com/v1/playlists/{playlist.ID}/tracks"
        response = self._post_request(url, data)
        json_response = response.json()
        return json_response

    # Creates a sub-playlist based on the given artist
    def createSubPlaylist(self, parentPlaylist, artist, subName):
        parentSongList = self.get_playlist(parentPlaylist.getID())
        subSongList =[]
        for song in parentSongList:
            if song.getArtist() is artist:
                subSongList.append(song)
        subPlaylist = self.create_playlist(subName)

    # Creates new playlists to sort existing playlists by genre
    def sortByGenre(self, playlists):
        playlists_by_genre = {}
        for playlist in playlists:
            name = playlist['name']
            genres = playlist['genres']
            for genre in genres:
                if genre in playlists_by_genre:
                    playlists_by_genre[genre].append(name)
                else:
                    playlists_by_genre[genre] = [name]

        # Sort the dictionary the genres
        sorted_playlists_by_genre = sorted(playlists_by_genre.items())