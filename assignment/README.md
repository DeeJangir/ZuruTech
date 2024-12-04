# PyLS - Python Listing Utility

`pyls` is a Python-based utility to list directory contents, similar to the Unix `ls` command. It parses a JSON file representing a directory structure and provides various listing options like filtering, sorting, and recursive display.

---

## Features

- List files and directories from a JSON structure.
- Support for Unix-style flags:
  - `-A`: Include hidden files.
  - `-l`: Long listing format with details (permissions, size, modification time).
  - `-r`: Reverse the order of listing.
  - `-t`: Sort by time modified (newest first).
  - `-H`: Show list of content with file/directory size in human readable format.
- Filter files or directories using `--filter=dir` or `--filter=file`.
- file: file path to operate over
- Handle non-existent paths gracefully.
- Fully customizable and extendable.

---

## Commands to run program
```python -m pyls -A -l -r --file "assignment/structure.json" -H parser```

- to install program using pip
```pip install -e . [should be executed in directory where pyproject.toml is placed]```
- after this you can run program without python -m
```pyls -A -l -r --file "assignment/structure.json" -H parser```

## Directory Structure JSON Format

The input JSON file should represent the directory structure with the following keys:
- `name`: Name of the file/directory.
- `size`: Size of the file/directory in bytes.
- `time_modified`: UNIX timestamp of the last modification.
- `permissions`: Permissions string (e.g., `-rw-r--r--` for files, `drwxr-xr-x` for directories).
- `contents`: (Optional) Array of nested files or directories for directories.

### Example JSON

```json
{
  "name": "root",
  "size": 4096,
  "time_modified": 1699957865,
  "permissions": "drwxr-xr-x",
  "contents": [
    {"name": "file1.txt", "size": 1024, "time_modified": 1699941437, "permissions": "-rw-r--r--"},
    {"name": "subdir", "size": 4096, "time_modified": 1699957739, "permissions": "drwxr-xr-x", "contents": []}
  ]
}

