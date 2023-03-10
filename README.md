# Beginner-Friendly-File-Searcher
Easier, User-Friendly, File Searcher

## Download
Stable Releases:
- Windows 64x
- GCP 5.15.0-1025 (portable only)

Beta Releases:
- Certain Linux Distros with "Windows-like" Commands
- Windows 32x

Instalation: 
```
1. Run filesearcher.exe when downloading latest version.
```

Portable Installation Steps
```
For Windows 64x or Beta Releases:
0. Download Python3
1. Download main.py
2. Move to either:
  - C:
  - /dir/searchingdir/
3. To run, simply run this script in your shell after navigating to where you have installed the file: 

python3 main.py

Note: If there are any issues with this function, check for any other python files titled "main.py". You can rename this main.py file but then make sure to use the suitable file name for python3 command.

For GCP 5.15.0-1025 (replit)
Download and Port the Entire Repository
Rename your main.py to "BFS.py"
To use, go into the ".replit" folder and change the entrypoint from "main.py" to "BFS.py".

```

## Background
Coming from Linux, this function was a little too much and hard to find suitable information: 
```
where /r <file/folderlocation> *<file/foldername>* | clip
```
I'd decided to test my Python skills by creating an User-Friendly (UI-ish) function for Windows CMD/Powershell to find your files easier. As long as your search query contains the keyword/letters, then it should be able to find your file!
