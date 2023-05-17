# TikTok-PostTracker
The TikTok PostTracker is a Python script that allows you to track and automatically download the most recent video from a TikTok user's profile. It utilizes web scraping techniques to extract the video URL and then downloads the video using the ssstik.io service.

**Prerequisites**
Python 3.x
requests library
beautifulsoup4 library
urllib library


**Setup**
Install the required libraries:

requests: A library for making HTTP requests.
beautifulsoup4: A library for parsing HTML and XML documents.
urllib: A library for handling URLs and file downloading.
Import the necessary libraries:

requests: Import the requests module for making HTTP requests.
beautifulsoup4: Import the BeautifulSoup module for parsing HTML documents.
urllib: Import the urlopen and Request functions for downloading files.

**Usage**
Specify the TikTok profile username:

Set the username variable to the TikTok profile username you want to track and download videos from.
Specify the save directory:

Set the save_dir variable to the directory path where you want to save the downloaded videos.
If the directory does not exist, the script will create it automatically.
Specify the path to the downloaded videos file:

Set the downloaded_videos_file variable to the path of the text file where the script will keep track of the downloaded videos.
If the file does not exist, the script will create it automatically.
Run the script:

Execute the script and it will start monitoring the TikTok user's profile for new videos.
It will check for the most recent video at regular intervals (every 30 seconds by default).
If a new video is found, it will download the video and save it to the specified directory.
The downloaded video URL will be recorded in the downloaded videos file to avoid downloading duplicates.
Stop the script:

To stop the script, you can terminate the program manually.


**Limitations**
The script relies on the structure of the TikTok website and the ssstik.io service, so any changes to these platforms may break the scraping and downloading process.
The script does not handle exceptions or errors gracefully. Additional error handling and validation should be implemented for a more robust solution.
The script assumes that the downloaded videos file is formatted as a simple text file with one video URL per line.

**Disclaimer**
Please be aware of the legal implications of web scraping and video downloading. Make sure to review and comply with TikTok's terms of service and respect the privacy of users.
Use this script responsibly and in accordance with TikTok's terms of service and any applicable laws and regulations.




