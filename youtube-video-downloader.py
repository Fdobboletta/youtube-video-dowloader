import tkinter as tk
from tkinter import messagebox
import yt_dlp

def download_video(video_url, output_path='video.mp4'):
    ydl_opts = {
        'format': 'best',
        'outtmpl':  f"{output_path}.%(ext)s"
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        try:
            ydl.download([video_url])
            messagebox.showinfo("Success", "Video downloaded successfully!")
        except Exception as e:
            messagebox.showerror("Error", f"Error downloading video: {e}")

def convert_mp4_to_mp3(video): 
    return

def create_gui():
    def on_download():
        video_url = url_input.get()
        file_name = file_name_input.get()

        if video_url:
            download_video(video_url, file_name)
        else:
            messagebox.showwarning("Warning", "Please enter a valid video URL.")

    # Create the main window
    root = tk.Tk()
    root.title("YouTube Video Downloader")
    

    # Input section
    file_name_input_label = tk.Label(root, text="Enter desired file name")
    file_name_input_label.pack(pady=10)
    file_name_input = tk.Entry(root, width=50)
    file_name_input.pack(pady=5)
    url_input_label = tk.Label(root, text="Enter YouTube Video URL:")
    url_input_label.pack(pady=10)
    url_input = tk.Entry(root, width=50)
    url_input.pack(pady=5)


    # Download button
    download_button = tk.Button(root, text="Download Video", command=on_download)
    download_button.pack(pady=10)

    root.mainloop()

if __name__ == "__main__":
    create_gui()
