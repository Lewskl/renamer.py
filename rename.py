# rename.py
# Copyright (c) 2018 Leevi Aaltonen
# renames all files in a folder or list

from pathlib import Path


def rename(files, nformat, start=1, test=False):
    """
    files should be a path to a directory or a list or tuple of file paths
    nformat should be a string containing the string "{#}" to represent the number
    start should be an integer
    """

    if not files:
        raise ValueError("files cannot be empty")

    if not nformat:
        nformat = "{num:0{numl}d}"
    elif not isinstance(nformat, str):
        raise TypeError("Expected string for nformat, got " + type(nformat).__name__)
    elif "{#}" not in nformat:
        raise ValueError("nformat must contain \"{#}\"")
    else:
        nformat = nformat.replace("{#}", "{num:0{numl}d}")

    if not start or not isinstance(start, int):
        raise TypeError("Expected integer for start, got " + type(start).__name__)

    if isinstance(files, Path):
        if files.is_dir():
            files = [file for file in files.iterdir() if file.is_file()]
        else:
            raise ValueError("files must point to a directory")

    elif not isinstance(files, (list, tuple)):
        raise TypeError("Must be a path to a directory or a list or tuple of file path objects")

    numl = len(str(len(files))) + start - 2  # pad with zeroes to the length of the largest number
    for i in range(0, len(files)):
        with files[i] as file:
            if test:
                print(file.with_name(nformat.format(num=i + start, numl=numl) + file.suffix))
            else:
                file.rename(file.with_name(nformat.format(num=i + start, numl=numl) + file.suffix))
