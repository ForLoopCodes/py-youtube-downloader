# import the module
from pytube import YouTube
import os

os.system('cls')
print("⭐ YouTube Video Downloader")
print("")
print("#️⃣  Note: Right click in the terminal to paste any links.")
print("📂 Specify the save path for the video. (Default: C:/Users/"+os.getlogin()+"/Desktop)")
path = input("1️⃣  ")

print("🔗 Enter the YouTube video link. (Right-click to paste):")
link = input("2️⃣  ")
if not link:
    print("❎ No link provided. Exiting.")
    exit()

print("📺 Enter the download resolution. (Dafault: 480p, or any other available)")
resolution = input("3️⃣  ")

print("🚀")
print("🔄️ Downloading: "+YouTube(link).title)

yt = YouTube(link)
video = yt.streams.filter(res=resolution).first() if resolution else yt.streams.filter(res="480p").first()

video.download(path if path else "C:/Users/"+os.getlogin()+"/Desktop")

print("✅ Downloaded successfully.")
print("📂 Open path: "+(path if path else "C:/Users/"+os.getlogin()+"/Desktop"))
