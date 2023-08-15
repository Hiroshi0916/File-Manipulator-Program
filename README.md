# Backend Project（File-Manipulator-Program)
## Application-OS Interaction Projects

This repository houses a collection of projects that explore how application programs interact with the operating system. It showcases both memory-based techniques, like pipes, and storage-based techniques, such as accessing and manipulating data stored in the Linux filesystem.

## Table of Contents
1. [Markdown to HTML Converter](#1markdown_to_html_converter)
2. [RandomNumber](#2randomnumber)
3. [File Manipulator](#3file-manipulator)


## 1. Markdown to HTML Converter

### Overview
This project provides a tool to convert Markdown files to HTML format. It also offers a feature to replace all full-width colons with half-width ones in the converted HTML content.

### Features
- Convert `.md` files to `.html`.
- Replace full-width colons `：` with half-width colons `:`.

### Usage
```bash
python3 Markdown_to_HTML_Converter.py markdown inputfile.md outputfile.html
```

## 2. RandomNumber

### Overview
A simple number guessing game. The program will randomly choose a number within a specified range, and the user has to guess it within a limited number of attempts.

### Features
- User can specify the range of numbers.
- User has ten attempts to guess the correct number.
- Informative prompts guiding the user throughout the game.

### Usage
```bash
python3 RandomNumber.py
```

## 3. File Manipulator

### Overview
The File Manipulator project offers a range of functionalities to manipulate the content of files. It supports actions like reversing the contents, copying files, duplicating content, and replacing specific strings.

### Features
- Reverse the content of a file and save it to another.
- Copy content from one file to another.
- Duplicate the content of a file a specified number of times.
- Replace specific substrings in a file.

### Usage
- For reversing contents:
```bash
python3 file_manipulator.py reverse input.txt output.txt
```

- For copying:
```bash
python3 file_manipulator.py copy input.txt output.txt
```
- For duplicating contents:
```bash
python3 file_manipulator.py duplicate-contents input.txt 3
```
- For replacing strings:
```bash
python3 file_manipulator.py replace-string input.txt oldstring newstring
```

