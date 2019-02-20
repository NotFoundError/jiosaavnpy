"""Get a tuple of song names by searching the jiosaavn page."""

from json import JSONDecoder
from bs4 import BeautifulSoup
import requests

from jiosaavnpy.saavn.songmeta import JioSaavnSong


class SearchJioSaavn:
    """
    Search JioSaavn page for the passed song name.
    """

    def __init__(self, name, songType):
        """
        name: Name of the song to search.
        """
        self._URL_PREPEND = "https://www.jiosaavn.com/search/{}"
        self.headers = {
                    'User-Agent': 'Mozilla/5.0 \
                                   (X11; Ubuntu; Linux x86_64; rv:49.0)\
                                   Gecko/20100101 Firefox/49.0'
                       }
        self.name = name
        self.results = []
        self.songType = songType
        self.act()

    def act(self):
        """
        Act according to the songType.
        """
        if self.songType == 'name':
            URL = self._URL_PREPEND.format(self.name)
            self._search(URL)
        elif self.songType == 'URL':
            self._search(self.name)
            self.results = self.results[0]

    def _search(self, URL):
        """
        Get the search page of jiosaavn and scrap it to get the data.
        """
        response = requests.get(URL, headers=self.headers)
        soup = BeautifulSoup(response.text, 'lxml')
        songs = soup.find_all('div', {'class': 'hide song-json'})

        for i in songs:
            obj = JSONDecoder().decode(i.text)
            jiosaavnsong = self._dump_data(obj)
            self.results.append(jiosaavnsong)

    def _dump_data(self, obj):
        """
        Dump the song metadat from obj to a JioSaavnSong object.
        """
        songmetaObj = JioSaavnSong(
                                    obj['title'],
                                    obj['singers'],
                                    obj['album'],
                                    obj['year'],
                                    obj['image_url'],
                                    obj['url']
                                      )
        return songmetaObj
