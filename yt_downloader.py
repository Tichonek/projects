#script to download *.mp4 or *.mp3 files from YouTube. 

from pytube import YouTube, exceptions
import os

def check_exists(video, extension):
    """Funciotn checks if file with extension(.mp3 or .mp4 given as an extesnion argument) exists in current working directory. Returns True or False"""
    
    #get video's title from YouTube link
    file = video.title

    #get current working directory and dir list
    cwd = os.getcwd()
    dirs = os.listdir(cwd)

    #change filename to filename.extension
    base, ext = os.path.splitext(file)
    name_with_ext = base + extension

    #check if file.mp3 is in current working directory
    if name_with_ext in dirs:
        is_in_directory = True
    else:
        is_in_directory = False

    return is_in_directory


def rename_to_mp3(out_file):
    """Function renames filename to filename.mp3"""

    #change filename to filename.mp3
    base, ext = os.path.splitext(out_file)
    new_file = base + ".mp3"
    try:
        os.rename(out_file, new_file)
    except FileExistsError:
        print(f"{new_file} already exists")
    else:
        return new_file

def download_mp4():
    """Downloading video from YouTube in highest avaliable resolution (720p or lower)."""
    
    url = input("Enter URL: ")
    video = YouTube(url)
    try:
        video = YouTube(url)

    except exceptions.VideoUnavailable:
        print(f"Video {url} ({video.title}) is unavaliable")

    except exceptions.RegexMatchError:
        print(f"The Regex pattern did not return any matches for the video: {url} ({video.title})")

    except exceptions.ExtractError:
         print(f"An extraction error occurred for the video: {url} ({video.title})")

    else:
        is_existing = check_exists(video, ".mp4")
        if is_existing:
            print(f"File '{video.title}.mp4' exists")
        else:
            print(f"Downloading mp4 file: {url} ({video.title})")
            video.streams.get_highest_resolution().download()
            print(f"Successfully downloaded {url} ({video.title})")


def download_mp3():
    """Downloading *.mp3 from YouTube """
    
    url = input("Enter URL: ")
    video = YouTube(url)

    try:
        video = YouTube(url)

    except exceptions.VideoUnavailable:
        print(f"Video {url} ({video.title}) is unavaliable")

    except exceptions.RegexMatchError:
        print(f"The Regex pattern did not return any matches for the video: {url} ({video.title})")

    except exceptions.ExtractError:
         print(f"An extraction error occurred for the video: {url} ({video.title})")
    
    else:
        is_existing = check_exists(video, ".mp3")
        if is_existing:
            print(f"File '{video.title}.mp3' exists")
        else:
            print(f"Downloading mp3 file: {url} ({video.title})")
            
            #downloading only audio
            audio_file = video.streams.filter(abr="160kbps", progressive=False).first()
            out_file = audio_file.download()

            #rename to file.mp3
            new_file = rename_to_mp3(out_file)

            print(f"Successfully downloaded!")
        

def main():
    choice = None
    while choice != "0":
        print(
            """
            0 - exit
            1 - download mp4
            2 - download mp3
            """
        )
        choice = input("Option: ")
        if choice == "0":
            break
        elif choice == "1":
            download_mp4()
        elif choice == "2":
            download_mp3()
        else:
            print("Bad option")

main()