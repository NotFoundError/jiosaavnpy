"""All the work related to songs."""

from jiosaavnpy.saavn.saavn_downloader import get_download_URL
from jiosaavnpy.saavn.utility import GetChoice
from jiosaavnpy.song.search import SearchJioSaavn
from jiosaavnpy.downloader import downloader
from jiosaavnpy.downloader import metadata


class Song:
    """Takes two arguments.

    entity: The name/URL (whatever is passed)
    entity_type: Type of the entity passed (name/URL)
    """

    def __init__(self, entity, entity_type):
        self.entity = entity
        self.type = entity_type
        self.choice = 0

    def _song_by_name(self):
        """Search the song online, ask the user for an option
        and download the choosen song.
        """
        result = SearchJioSaavn(self.entity, 'name').results
        self.choice = GetChoice(result).choice
        # Download the song now
        dwURl = get_download_URL(result[self.choice].url)
        # Pass the dwURL to be downloaded.
        des = downloader.download(dwURl, name=result[self.choice].title)
        # Set the metadata
        if des is not False:
            metadata.SetMetadata(des, result[self.choice])

    def _song_by_URL(self):
        """
        Extract the meta info from the site and get the encrypted URL.
        """
        result = SearchJioSaavn(self.entity, 'URL').results
        dwURL = get_download_URL(result.url)
        downloader.download(dwURL)
        # print(dwURL, 'is the URL of the passed song!')

    def act(self):
        """Act according to the type."""
        if self.type == 'name':
            self._song_by_name()
        elif self.type == 'URL':
            self._song_by_URL()
