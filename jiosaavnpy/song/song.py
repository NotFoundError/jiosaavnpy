"""All the work related to songs."""

from jiosaavnpy.saavn.saavn_downloader import get_download_URL
from jiosaavnpy.saavn.utility import GetChoice
from jiosaavnpy.song.search import SearchJioSaavn
from jiosaavnpy.downloader import downloader
from jiosaavnpy.downloader import metadata

from jiosaavnpy.logger import Logger

# Setup logger
logger = Logger('song')


class Song:
    """Takes two arguments.

    entity: The name/URL (whatever is passed)
    entity_type: Type of the entity passed (name/URL)
    """

    def __init__(self, entity, entity_type):
        self.entity = entity
        self.type = entity_type
        self.choice = 0
        self.result = []
        self._get_song()
        self._download()

    def _get_song(self):
        """
        Search the song online, ask the user for an option
        and download the choosen song.
        """
        self.result = SearchJioSaavn(self.entity, self.type).results
        if self.type == 'name':
            self.choice = GetChoice(self.result).choice
        elif self.type == 'URL':
            self.choice = 0

    def _download(self):
        # Download the song now
        dwURl = get_download_URL(self.result[self.choice].url)
        # Pass the dwURL to be downloaded.
        des = downloader.download(dwURl, name=self.result[self.choice].title)
        logger.info('Song downloaded to {}'.format(des))
        # Set the metadata
        if des is not False:
            metadata.SetMetadata(des, self.result[self.choice])
