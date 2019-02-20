"""File to define a class that stores the song data."""


class JioSaavnSong:
    """
        title: Title of the song
        artist: Artist of the song
        album: Album name of the song
        releaseDate: Release date of the song
        artwork: URL to the artwork
        url: URL of the song that will be used to download it
        trackNumber: Number of the track in the album
    """

    def __init__(
                self,
                title,
                artist,
                album,
                releaseDate,
                artwork,
                url,
                trackNumber='1'
                ):
        """Initiate the data."""
        self.title = title
        self.artist = artist
        self.album = album
        self.releaseDate = releaseDate
        self.artwork = artwork
        self.url = url
        self.trackNumber = trackNumber
