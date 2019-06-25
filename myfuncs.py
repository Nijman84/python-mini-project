import errno
from os import remove


def silentremove(file_name):
    try:
        remove(file_name)
    except OSError as e:
        if e.errno != errno.ENOENT:
            raise
