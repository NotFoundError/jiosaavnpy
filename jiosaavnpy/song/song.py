"""All the work related to songs."""

from jiosaavnpy.saavn.saavn_downloader import get_download_URL


class Song:
    """Takes two arguments.

    entity: The name/URL (whatever is passed)
    entity_type: Type of the entity passed (name/URL)
    """

    def __init__(self, entity, entity_type):
        self.entity = entity
        self.type = entity_type

    def _song_by_name(self):
        """Search the song online, ask the user for an option
        and download the choosen song.
        """

    def act(self):
        """Act according to the type."""
        if self.type == 'name':
            pass
