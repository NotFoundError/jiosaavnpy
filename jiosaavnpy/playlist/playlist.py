"""Functions related to playlist extraction are defined."""

from jiosaavnpy.song.search import SearchJioSaavn
from jiosaavnpy.song.song import Song

from jiosaavnpy.logger import Logger

# Setup logger
logger = Logger('playlist')


class JioSaavnPlaylist:
    """
    Class to extract JioSaavn Playlists playlists
    and download the songs.
    As of now two types of URL's are considered
    playlist links.
    One with **/featured/** on the URL
    One with **/playlist/** on the URL

    featured ones are the playlists made by JioSaavn
    playlist ones are the ones made by users.
    """

    def __init__(self, URL):
        self.URL = URL
        self.headers = {
                    'User-Agent': 'Mozilla/5.0 \
                                   (X11; Ubuntu; Linux x86_64; rv:49.0)\
                                   Gecko/20100101 Firefox/49.0'
                       }
        self.content_tuple = []
        self._extract_content()

    def _extract_content(self):
        """
        Extract the page contents using the SearchJioSaavn
        class.
        """
        logger.info('Extracting playlist content.')
        self.content_tuple = SearchJioSaavn(self.URL, 'URL').results

        for i in self.content_tuple:
            # Each song can be thought of as URL downloadable entity
            logger.info('Downloading {} by {}'.format(i.title, i.artist))
            Song(i.perma_url, 'URL')
