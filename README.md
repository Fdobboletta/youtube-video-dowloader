# YouTube Video Downloader

A simple Python GUI application using tkinter and yt-dlp to download YouTube videos.

## Overview

This project provides a graphical user interface (GUI) for downloading YouTube videos. It uses the yt-dlp library, which is an enhanced version of youtube-dl, to fetch and save videos from YouTube.

## Features

- **Download YouTube Videos**: Enter a YouTube video URL and specify the output filename to download the video in MP4 format.
- **GUI Interface**: Built using tkinter, providing a straightforward interface for users to input URLs and filenames.
- **Error Handling**: Displays error messages if there are issues with downloading the video.

## Installation

Follow these steps to set up and run the YouTube Video Downloader:

### Prerequisites

- Python 3.6 or higher installed on your system.

### Clone the Repository

```bash
git clone https://github.com/Fdobboletta/youtube-video-dowloader.git
cd youtube-video-downloader
```

````

### Install Dependencies

Make sure you have all dependencies installed. It's recommended to set up a virtual environment first:

```bash
python -m venv env
source env/bin/activate   # On Windows use `env\Scripts\activate`
pip install -r requirements.txt
```

## Run the Application

Run the following command to start the GUI:

```bash
python youtube-video-downloader.py
```

## Usage

1. Launch the application.
2. Enter the desired filename for the downloaded video.
3. Paste the YouTube video URL into the input field.
4. Click the "Download Video" button to initiate the download.
5. Once completed, a success message will confirm the download.


## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvement, please open an issue or submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

````
