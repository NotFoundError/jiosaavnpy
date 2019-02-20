import urllib.request
import sys
import time
from os import path, popen


def get_terminal_length():
    """Return the length of the terminal."""
    rows, cols = popen('stty size', 'r').read().split()

    return int(cols)


def download(url, verbose=True, name='', desfol='~/Music'):
    try:
        if name == '':
            name = url.split('/')[-1]
        else:
            if name.split('.')[-1] != 'mp3':
                name = name + '.mp3'
        des = path.join(path.expanduser(desfol), name)
        # Download files with a progressbar showing the percentage
        u = urllib.request.urlopen(url)
        f = open(des, 'wb')
        meta = u.info()

        file_size = int(meta["Content-Length"])

        file_size_dl = 0
        block_sz = 8192

        beg_time = time.time()
        while True:
            buffer = u.read(block_sz)
            if not buffer:
                break

            file_size_dl += len(buffer)
            f.write(buffer)

            if verbose:
                # Calculate speed
                speed = (file_size_dl / 1024) / (time.time() - beg_time)

                # Calculate time left
                time_left = round(((file_size - file_size_dl) / 1024) / speed)
                time_unit = 's'

                # Convert to min or hours as req
                if time_left > 3600:
                    time_left = round(time_left / 3600)
                    time_unit = 'h'
                elif time_left > 60:
                    time_left = round(time_left / 60)
                    time_unit = 'm'

                # Calculate percentage
                percent = file_size_dl * 100. / file_size

                # file_size to show
                if file_size_dl > (1024 * 1024):
                    file_size_to_disp = file_size_dl / (1024 * 1024)
                    dw_unit = "MB's"
                elif file_size_dl > 1024:
                    file_size_to_disp = file_size_dl / 1024
                    dw_unit = "kb's"

                # Basename
                basename = path.basename(des)

                # Calculate amount of space req in between
                length = get_terminal_length()

                stuff_len = len(basename) + 13 + 17 + 7 + 26 + 5
                space = 0

                if stuff_len < length:
                    space = length - stuff_len
                elif stuff_len > length:
                    basename = basename[:(length - stuff_len) - 2] + '..'

                status = r"%s %s %0.2f %s |%d kbps| ETA: %s %s |%-20s| %3.2f%%" % (basename, space * " ", file_size_to_disp, dw_unit, speed, time_left, time_unit, "-" * int(percent / 5), percent)
                sys.stdout.write('\r')
                sys.stdout.write(status)
                sys.stdout.flush()

        f.close()

        if verbose:
            print()
        return des
    except ConnectionError:
        print("Connection Error!")
        return False


if __name__ == "__main__":
    download("http://speedtest.ftp.otenet.gr/files/test100k.db", 'nana.mkv')
