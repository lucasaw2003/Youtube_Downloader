from pytube import YouTube
from gi.repository import GLib

link = input("Insert Link: ")

try: 
    yt = YouTube(link)
    downloads_dir = GLib.get_user_special_dir(GLib.UserDirectory.DIRECTORY_DOWNLOAD)
    save_video_path = f"{downloads_dir}"
    output_file_name = f"{yt.title}.mp4"
    stream = yt.streams.get_by_itag(22)
    stream.download(output_path = save_video_path, filename = output_file_name)
    print(f"YouTube video download successfully at {save_video_path} and file name is {output_file_name}.")
    pass
except: 
    print("Invalid URL")
    pass

