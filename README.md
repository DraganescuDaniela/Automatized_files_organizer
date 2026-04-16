# File Organizer Script

A small Python project I made to automatically sort files into folders based on their extension. I got tired of my Desktop being a mess so I decided to automate it.

---

## What it does

- Looks at all the files in a folder you specify
- Moves them into subfolders based on their extension (`.pdf` goes to `PDF_Files`, `.jpg` goes to `Images`, etc.)
- If a file with the same name already exists in the destination, it saves it as `filename_copy.ext` instead of overwriting it
- Keeps a log file with timestamps so you can see what was moved (or what broke)

---

## Folder structure

```
python-document-automation/
│
├── organizer.py          # the main script
├── log.txt               # gets created automatically when you run it
│
├── test_folder/          # put the files you want to organize here
│
└── organized/            # sorted files end up here (also created automatically)
    ├── PDF_Files/
    ├── Images/
    ├── Word_Documents/
    ├── Text_Files/
    └── Others/
```

---

## File sorting rules

| Extension         | Goes to folder    |
|-------------------|-------------------|
| `.pdf`            | `PDF_Files`       |
| `.jpg`, `.png`    | `Images`          |
| `.docx`           | `Word_Documents`  |
| `.txt`            | `Text_Files`      |
| anything else     | `Others`          |

You can add more file types by editing the `reguli` dictionary at the top of the script.

---

## How to run it

You just need Python 3 installed, no extra libraries needed.

First, open `organizer.py` and change these three paths at the bottom to match your own folders:

```python
folder_t    = r"C:\Path\To\source_folder"
folder_dest = r"C:\Path\To\organized"
mesaj       = r"C:\Path\To\log.txt"
```

Then just run it:

```bash
python organizer.py
```

That's it. Check the `organized` folder and `log.txt` afterwards.

---

## Log example

```
2025-04-16 14:32:01: Moved report.pdf -> PDF_Files
2025-04-16 14:32:01: Moved photo.jpg -> Images
2025-04-16 14:32:01: ERROR with some_file -> [Errno 13] Permission denied
```

---

## Notes

- The script only moves files, not subfolders
- I only handle one level of duplicate (so if both `file.pdf` and `file_copy.pdf` already exist, it'll log an error)
- The folder names are in Romanian because that's how I named them (`reguli` = rules, `organizare_fisiere` = file organizer, etc.)

---

## Requirements

- Python 3.6+
- No external libraries (only `os`, `shutil`, `datetime` from the standard library)
