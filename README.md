# 📁 File Organizer — Smart File Sorter

Automatically organizes messy folders by sorting files into categorized folders based on their type.

---

## ✨ Features

- 🔍 **Smart Categorization** — Sorts files into logical folders (Images, Documents, Videos, etc.)
- 🔄 **Duplicate Handling** — Automatically renames duplicate files to avoid overwriting
- 🎯 **Leaves Folders Intact** — Only sorts files, doesn't touch existing subfolders
- 📊 **Detailed Summary** — Shows what was moved and which folders were created
- 🛡️ **Safe Operation** — Asks for confirmation before making any changes
- 📦 **No Dependencies** — Uses Python 3.6+ standard library only

---

## 🚀 Quick Start

1. Save `sort_files.py` to your computer
2. Open terminal or command prompt
3. Run: `python sort_files.py "/path/to/your/folder"`
4. Type `yes` when prompted — done!

---

## 💻 Usage

**Windows:**
```bash
python sort_files.py "C:\Users\username\Downloads"
python sort_files.py "D:\My Documents\Unsorted"
```

**Linux / macOS:**
```bash
python sort_files.py "/home/username/Downloads"
python sort_files.py "~/Desktop/Unsorted"
```

---

## 📂 File Categories

| Category      | Extensions                                              |
|---------------|---------------------------------------------------------|
| Images        | `.jpg` `.jpeg` `.png` `.gif` `.bmp` `.svg` `.webp` `.ico` |
| Videos        | `.mp4` `.avi` `.mkv` `.mov` `.wmv` `.flv` `.webm` `.m4v` |
| Music         | `.mp3` `.wav` `.flac` `.aac` `.ogg` `.m4a` `.wma`      |
| Documents     | `.pdf` `.doc` `.docx` `.txt` `.rtf` `.odt`              |
| Spreadsheets  | `.xls` `.xlsx` `.csv` `.ods`                            |
| Presentations | `.ppt` `.pptx` `.odp`                                   |
| Archives      | `.zip` `.rar` `.7z` `.tar` `.gz` `.bz2`                 |
| Code          | `.py` `.js` `.html` `.css` `.java` `.cpp` `.c` `.php` `.rb` `.go` `.json` `.xml` |
| Executables   | `.exe` `.msi` `.app` `.deb` `.rpm`                      |
| Others        | Any other extension → `EXTENSION_Files/` folder        |

---

## 📊 Example Output
```
📂 Target folder: C:\Users\username\Downloads
Continue with sorting? (yes/no): yes

Sorting files in: C:\Users\username\Downloads
==================================================
📁 Created folder: Images
✅ Moved: vacation.jpg → Images/
📁 Created folder: Documents
✅ Moved: report.pdf → Documents/
✅ Moved: notes.txt → Documents/
📁 Created folder: Music
✅ Moved: song.mp3 → Music/
==================================================
Summary: 4 files moved · 3 folders created
==================================================
```

---

## 🎨 Customization

**Rename a category:**
```python
return "Pictures"  # instead of "Images"
```

**Add new file extensions:**
```python
elif extension in ['jpg', 'jpeg', 'png', 'gif', 'raw', 'psd']:
    return "Images"
```

**Create a new category:**
```python
elif extension in ['iso', 'img', 'dmg']:
    return "Disk_Images"
```

---

## 🔧 Troubleshooting

| Error | Fix |
|-------|-----|
| `Directory does not exist` | Check the folder path; use absolute paths |
| `Permission denied` | Ensure you have write access; close any apps using the files |
| Files not moving | Files may already be sorted; the script skips organized files |

---

## 📝 Notes

- Only files are moved — existing subfolders remain untouched
- Duplicate files are renamed with a number suffix (e.g. `file_1.txt`)
- The operation can be cancelled before any changes are made

---

## 📄 License

MIT License — free for personal and commercial use.

## Vibe Coded but features and idea are mine and fixed some error
