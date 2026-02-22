# File Organization Automation Tool

A Python CLI script to automatically move files containing a specific substring from source directory to destination directory.

## Problem It Solves

Imagine you have 100 files in your Downloads folder:
- `report_2024_jan.pdf`
- `report_2024_feb.pdf`
- `vacation_photo.jpg`
- `report_2024_mar.pdf`

Instead of manually moving all "report" files, this script does it automatically!

## Features

- ✅ Move multiple files matching a pattern in one command
- ✅ Cross-platform path handling (works on Windows, Mac, Linux)
- ✅ Simple CLI interface with argparse
- ✅ Safe file operations using shutil

## Installation

1. Clone the repository:
```bash
git clone https://github.com/nivelone/Move_file_to_path_Automation_script.git
cd Move_file_to_path_Automation_script
```

2. No external dependencies required (uses Python standard library)

## Usage

### Basic Syntax:
```bash
python move_files.py <source_path> <filename_substring> <destination_path>
```

### Examples:

**Example 1: Move all PDF reports**
```bash
python move_files.py "C:/Downloads/" "report" "C:/Documents/Reports/"
```
This moves all files containing "report" from Downloads to Documents/Reports

**Example 2: Organize photos**
```bash
python move_files.py "/Users/aman/Desktop/" ".jpg" "/Users/aman/Photos/"
```
This moves all .jpg files from Desktop to Photos folder

**Example 3: Move Python scripts**
```bash
python move_files.py "./projects/" ".py" "./python_files/"
```

### Parameters:

| Parameter | Description | Example |
|-----------|-------------|---------|
| `source_path` | Directory to search for files | `"C:/Downloads/"` |
| `filenamesubstring` | Pattern to match in filename | `"report"` or `".pdf"` |
| `destination_path` | Where to move matched files | `"C:/Reports/"` |

## How It Works

1. **Change to source directory**: `os.chdir(source_path)`
2. **List all files**: `os.listdir()` 
3. **Filter files**: Check if substring is in filename
4. **Move matched files**: `shutil.move()` to destination

## Code Structure
```python
def moveFilestodestination(source_path, filenamesubstring, destination_path):
    # Changes to source directory
    # Loops through all files
    # Checks if substring matches
    # Moves matching files to destination
```

## Learning Outcomes

This project teaches:
- **File I/O operations** (os module)
- **File manipulation** (shutil module)
- **Command-line arguments** (argparse)
- **String operations** (substring matching)
- **Path handling** (cross-platform compatibility)

## Use Cases

- 📁 Organize downloads folder
- 📊 Sort project files by type
- 📧 Move email attachments
- 🎵 Organize music/video files
- 📝 Batch move documents

## Possible Improvements

- [ ] Add file extension filtering
- [ ] Implement recursive directory search
- [ ] Add dry-run mode (preview before moving)
- [ ] Create GUI version
- [ ] Add logging for moved files

## Requirements

- Python 3.6+
- No external packages (uses standard library only)

## Author

**Aman Singh Bhati**
- GitHub: [@nivelone](https://github.com/nivelone)
- Email: amanbhati2004@email.com

## License

MIT License - Feel free to use and modify

## Contributing

Pull requests welcome! Ideas for improvements:
- Better error handling
- Progress bar for large file moves
- Undo functionality
