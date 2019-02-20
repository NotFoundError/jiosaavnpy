"""Functions related to utility are defined."""

import re


class JioSaavnURL:
    """Class to check if a passed URL is related to JioSaavn."""

    def __init__(self, URL):
        self.URL = URL
        self.type = ''
        self._checkURL()

    def _checkURL(self):
        """Check the URL and update the URL type accordingly."""
        self._is_valid_URL()
        self._is_playlist_URL()

    def _is_valid_URL(self):
        """Check if the passed URL is a valid JioSaavn URL."""
        match = re.findall(r'^(https://www.)?(jio)?saavn\.com.*?$', self.URL)
        if match:
            self.type = 'song'

    def _is_playlist_URL(self):
        """Check if the passed URL is a JioSaavn playlist URL."""
        match = re.findall(r'(https://www.)?(jio)?saavn.com/(s/playlist|featured)/.*?', self.URL)
        if match:
            self.type = 'playlist'


class GetChoice:
    """
    Class to get choice from user.

    A tuple is supposed to be passed.
    """

    def __init__(self, contentTuple):
        self.contentTuple = contentTuple
        self.choice = 0
        self._diplay_options()
        self._get_choice()

    def _diplay_options(self):
        """
        Display the options.
        """
        for i in range(0, len(self.contentTuple)):
            print('[{}] {} by {}'.format(i + 1, self.contentTuple[i].title, self.contentTuple[i].artist))

    def _get_choice(self):
        """
        Get the choice from the user.
        """
        while True:
            choice = int(input("Enter choice [a valid one] "))
            choice -= 1
            if self.choice in range(0, len(self.contentTuple)):
                break


if __name__ == '__main__':
    url = "https://www.jiosaavn.com/song/qaafirana/BTs0Wi5cUV0"
    url1 = "https://www.saavn.com/s/playlist/671dda9e31ee5c52ee7d7a91a52b38cc/FavSongs/ls,AsKJkwiIGSw2I1RxdhQ__"
    print(JioSaavnURL(url1).type)
