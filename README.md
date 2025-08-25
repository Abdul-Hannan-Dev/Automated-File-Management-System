# Automated-File-Management-System# Automated File Management System

## 📌 Overview

The **Automated File Management System** is a Python-based utility that organizes files from a user-specified directory into categorized folders. It sorts files into directories like **Images**, **Videos**, **Documents**, **TextFiles**, and **Others**, while maintaining a log of every transfer.

This helps keep directories clean and ensures files are never duplicated — instead, new versions are renamed automatically.

---

## 🚀 Features

* Monitors and organizes any user-provided directory.
* Automatically detects file types using MIME types.
* Categorizes files into:

  * **Images**
  * **Videos**
  * **Applications/Documents**
  * **TextFiles**
  * **Others**
* Prevents overwriting by renaming duplicate files.
* Maintains a timestamped **log file** for each monitored directory.

---

## 🛠️ Requirements

* Python 3.8+
* Dependencies:

  ```bash
  pip install platformdirs
  ```

> All other imports (`os`, `shutil`, `datetime`, `mimetypes`, `re`) are part of Python’s standard library.

---

## ▶️ Usage

1. Clone or download the project.
2. Run the script:

   ```bash
   python file_manager.py
   ```
3. Enter the **full path** of the directory you want to organize (e.g., `C:\Users\YourName\Downloads`).
4. The script will automatically transfer and organize files into their respective folders.

---

## 📂 Example

If you enter the path:

```
C:\Users\Hannan\Downloads
```

* Images move to `Pictures/`
* Videos move to `Videos/`
* Applications/Documents move to `Documents/`
* Text files move to `Documents/TextFiles/`
* Others go to `Documents/Others/`

A log file will be created as:

```
data_Downloads.txt
```

containing records of each transfer with a timestamp.

---

## ✨ Future Improvements

* Add real-time monitoring (using `watchdog`).
* Provide a GUI for easier user interaction.
* Support custom category mappings.


