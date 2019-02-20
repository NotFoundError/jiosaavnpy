"""Get a tuple of song names by searching the jiosaavn page."""

from json import JSONDecoder
from bs4 import BeautifulSoup
import requests

from jiosaavnpy.saavn.songmeta import JioSaavnSong


class SearchJioSaavn:
    """
    Search JioSaavn page for the passed song name.
    """

    def __init__(self, name):
        """
        name: Name of the song to search.
        """
        self._URL_PREPEND = "https://www.jiosaavn.com/search/{}"
        self._URL = self._URL_PREPEND.format(name)
        self.headers = {
                    'User-Agent': 'Mozilla/5.0 \
                                   (X11; Ubuntu; Linux x86_64; rv:49.0)\
                                   Gecko/20100101 Firefox/49.0'
                       }
        self.results = []
        self._search()

    def _search(self):
        """
        Get the search page of jiosaavn and scrap it to get the data.
        """
        response = requests.get(self._URL, headers=self.headers)
        soup = BeautifulSoup(response.text, 'lxml')
        songs = soup.find_all('div', {'class': 'hide song-json'})

        for i in songs:
            obj = JSONDecoder().decode(i.text)
            songmetaObj = JioSaavnSong(
                                    obj['title'],
                                    obj['singers'],
                                    obj['album'],
                                    obj['year'],
                                    obj['image_url'],
                                    obj['url']
                                      )
            self.results.append(songmetaObj)
