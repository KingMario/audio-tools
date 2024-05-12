#!/usr/bin/env python3

import os
import sys

def rename_mp3_files(directory):
    """Rename mp3 files by prefixing the parent folder name."""
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".mp3"):
                if directory == '.':
                    parent_folder = os.path.basename(os.path.abspath(root))
                else:
                    parent_folder = os.path.basename(root)
                new_filename = f"{parent_folder}_{file}"
                original_path = os.path.join(root, file)
                new_path = os.path.join(root, new_filename)
                os.rename(original_path, new_path)
                print(f"Renamed '{original_path}' to '{new_path}'")

if __name__ == "__main__":
    if len(sys.argv) == 1:
        directory = '.'
    else:
        directory = sys.argv[1]
    if not os.path.isdir(directory):
        print("Error: The specified path is not a directory.")
        sys.exit(1)
    
    rename_mp3_files(directory)
