# Ari Hietanen
# Introduction to programming
# OS-library


def fix_filenames(folder):
    """
    This function renames .mp3 files in a folder with the format "number-artist-song_name.mp3" or "int-str-str"
    as "song_name-artist.mp3"
    :param folder: The name of a folder that includes the files to be renamed
    :type folder: str
    :return:
    """
    import os
    names = os.listdir(folder)
    os.chdir(folder)

    for file in names:

        if file.endswith(".mp3"):
            try:
                numbr, artist, song = file.split("-")
                numbr = int(numbr)  # Checks if the first
                song = song[:-4]
                os.rename(file, f"{song}-{artist}.mp3")
            except ValueError:
                continue
