"""Main function and other subfunctions defined."""

import argparse

from jiosaavnpy.song.song import Song
from jiosaavnpy.saavn.utility import JioSaavnURL


def parse_arguments():
    """Parse the arguments."""
    parser = argparse.ArgumentParser(description="Download songs,\
                                    playlists, albums from JioSaavn directly.\
                                    Check (https://github.com/deepjyoti30/jiosaavnpy)\
                                    for more details.")

    parser.add_argument('entity',
                        help="Name of the song to search / URL of a playlist",
                        default=None, type=str)
    args = parser.parse_args()
    return args


def main():
    args = parse_arguments()
    URLtype = JioSaavnURL(args.entity).type

    if URLtype == 'playlist':
        # Do something
        pass
    elif URLtype == 'song':
        song = Song(args.entity, 'URL')
        song.act()
    else:
        # Its a song
        song = Song(args.entity, 'name')
        song.act()
