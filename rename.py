# rename.py
# by Leevi Aaltonen 2018
# renames all files in a folder or list

from pathlib import Path


def quickrename(files, start=1):
    # files should be a path to a directory or a list or tuple of file paths
    # start should be an integer

    if not files:
        raise ValueError("Empty path")

    if not start or not isinstance(start, int):
        raise TypeError("Expected integer for start, got " + type(start).__name__)

    if isinstance(files, Path):
        if files.is_dir():
            files = [file for file in files.iterdir() if file.is_file()]
        else:
            raise ValueError("files must ")

    elif not isinstance(files, (list, tuple)):
        raise TypeError("Must be a path to a directory or a list or tuple of file path objects")

    for i in range(0, len(files)):
        numl = len(str(len(files)))
        with files[i] as file:
            file.rename(file.with_name("ep" + "{num:0{numl}d}".format(num=i + start, numl=numl)))
