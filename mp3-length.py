#!/usr/bin/env python3

import os
import sys
from mutagen.mp3 import MP3

def get_mp3_files(directory):
    """Retrieve all mp3 files from the specified directory."""
    mp3_files = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".mp3"):
                mp3_files.append(os.path.join(root, file))
    return mp3_files

def sum_durations(mp3_files):
    """Calculate the total duration of a list of mp3 files."""
    total_seconds = 0
    for file in mp3_files:
        audio = MP3(file)
        total_seconds += audio.info.length
    return total_seconds

def format_duration(seconds):
    """Convert seconds to hh:mm:ss format."""
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    seconds = seconds % 60
    return f"{int(hours):02}:{int(minutes):02}:{int(seconds):02}"

if __name__ == "__main__":
    if len(sys.argv) == 1:
        directory = '.'
    else:
        directory = sys.argv[1]
    if not os.path.isdir(directory):
        print("Error: The specified path is not a directory.")
        sys.exit(1)
    
    mp3_files = get_mp3_files(directory)
    total_duration_seconds = sum_durations(mp3_files)
    formatted_duration = format_duration(total_duration_seconds)
    print(f"Total duration of all MP3 files: {formatted_duration}")
