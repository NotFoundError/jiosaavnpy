"""All the work related to songs."""

from jiosaavnpy.saavn.saavn_downloader import get_download_URL
from jiosaavnpy.saavn.utility import GetChoice
from jiosaavnpy.song.search import SearchJioSaavn


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
        result = SearchJioSaavn(self.entity).results
        self.choice = GetChoice(result).choice
        # Download the song now
        dwURl = get_download_URL(result[self.choice].url)
        print(dwURl, 'is the URL of the choosen song!')

    def act(self):
        """Act according to the type."""
        if self.type == 'name':
            self._song_by_name()

