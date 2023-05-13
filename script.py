import requests
import time
import os
from bs4 import BeautifulSoup
from urllib.request import urlopen, Request
from datetime import datetime

save_dir = 'path/to/save_directory'
if not os.path.exists(save_dir):
    os.makedirs(save_dir)

def get_recent_video_url(username):
    url = f"https://www.tiktok.com/@{username}"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    video_url = soup.find('div', {'class': 'tiktok-yz6ijl-DivWrapper'}).a['href']
    print(video_url)
    return video_url


def download_recent_video(username, save_dir, link):
    cookies = {
        '_ga': 'GA1.2.1922949325.1677776852',
        '_gid': 'GA1.2.2014378703.1677776852',
        '__gads': 'ID=f4cda8988d895a57-223f30f029dc0031:T=1677776853:RT=1677776853:S=ALNI_MZ3tLPUJ7FgeEyfTkZOclsQkY8QWQ',
        '__gpi': 'UID=00000be052f713af:T=1677776853:RT=1677776853:S=ALNI_MbvRQYg4RcYOg5bgCMetpAbh-8N7g',
        '_gat_UA-3524196-6': '1',
    }

    headers = {
        'authority': 'ssstik.io',
        'accept': '*/*',
        'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        # 'cookie': '_ga=GA1.2.1922949325.1677776852; _gid=GA1.2.2014378703.1677776852; __gads=ID=f4cda8988d895a57-223f30f029dc0031:T=1677776853:RT=1677776853:S=ALNI_MZ3tLPUJ7FgeEyfTkZOclsQkY8QWQ; __gpi=UID=00000be052f713af:T=1677776853:RT=1677776853:S=ALNI_MbvRQYg4RcYOg5bgCMetpAbh-8N7g; _gat_UA-3524196-6=1',
        'hx-current-url': 'https://ssstik.io/en',
        'hx-request': 'true',
        'hx-target': 'target',
        'hx-trigger': '_gcaptcha_pt',
        'origin': 'https://ssstik.io',
        'referer': 'https://ssstik.io/en',
        'sec-ch-ua': '"Not A(Brand";v="24", "Chromium";v="110"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Linux"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36',
    }

    params = {
        'url': 'dl',
    }

    data = {
        'id': link,
        'locale': 'en',
        'tt': 'MlNhdDQ1',
    }
    response = requests.post('https://ssstik.io/abc', params=params, cookies=cookies, headers=headers, data=data)
    downloadSoup = BeautifulSoup(response.text, 'html.parser')
    downloadURL = downloadSoup.a["href"]
    video_url = get_recent_video_url(username)
    if video_url in downloaded_videos:
        print(f"Skipping download of {video_url} as it has already been downloaded.")
        return
    filename = f"{username}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.mp4"
    filepath = os.path.join(save_dir, filename)
    if os.path.exists(filepath):
        print(f"Skipping download of {video_url} as {filepath} already exists.")
        downloaded_videos.append(video_url)
        return
    mp4_file = urlopen(downloadURL)
    with open(filepath, "wb") as f:
        while True:
            data = mp4_file.read(4096)
            if data:
                f.write(data)
            else:
                break
    downloaded_videos.append(video_url)
    print(f"Downloaded {video_url} to {filepath}")
    global latest_video_path
    latest_video_path = filepath

username = 'TikTok Profile Username'
save_dir = 'path/to/save_directory'
downloaded_videos_file = 'path/to/downloaded_videos.txt'

if not os.path.exists(save_dir):
    os.makedirs(save_dir)

if not os.path.exists(downloaded_videos_file):
    with open(downloaded_videos_file, 'w') as f:
        pass

with open(downloaded_videos_file, 'r') as f:
    downloaded_videos = [line.strip() for line in f.readlines()]

while True:
    video_url = get_recent_video_url(username)
    download_recent_video(username, save_dir, link=video_url)
    with open(downloaded_videos_file, 'a') as f:
        f.write(f"{video_url}\n")
    print("Running my script...")
    time.sleep(30)

