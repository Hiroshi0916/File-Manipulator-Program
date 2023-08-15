import sys
# import os

def reverse_contents(inputpath, outputpath):
    try:
        with open(inputpath, 'r') as f:
            content = f.read()
        reversed_content = content[::-1]
        with open(outputpath, 'w') as f:
            f.write(reversed_content)
    except Exception as e:
        print(f"Error: {e}")

def copy_file(inputpath, outputpath):
    try:
        with open(inputpath, 'r') as f:
            content = f.read()
        with open(outputpath, 'w') as f:
            f.write(content)
    except Exception as e:
        print(f"Error: {e}")

def duplicate_contents(inputpath, n):
    try:
        with open(inputpath, 'r') as f:
            content = f.read()
        duplicated_content = content * n
        with open(inputpath, 'w') as f:
            f.write(duplicated_content)
    except Exception as e:
        print(f"Error: {e}")

def replace_string(inputpath, needle, newstring):
    try:
        with open(inputpath, 'r') as f:
            content = f.read()
        replaced_content = content.replace(needle, newstring)
        with open(inputpath, 'w') as f:
            f.write(replaced_content)
    except Exception as e:
        print(f"Error: {e}")

def main():
    if len(sys.argv) < 3:
        print("Insufficient arguments!")
        return

    command = sys.argv[1]

    if command == "reverse":
        if len(sys.argv) != 4:
            print("Usage: reverse inputpath outputpath")
            return
        reverse_contents(sys.argv[2], sys.argv[3])
    elif command == "copy":
        if len(sys.argv) != 4:
            print("Usage: copy inputpath outputpath")
            return
        copy_file(sys.argv[2], sys.argv[3])
    elif command == "duplicate-contents":
        if len(sys.argv) != 4:
            print("Usage: duplicate-contents inputpath n")
            return
        duplicate_contents(sys.argv[2], int(sys.argv[3]))
    elif command == "replace-string":
        if len(sys.argv) != 5:
            print("Usage: replace-string inputpath needle newstring")
            return
        replace_string(sys.argv[2], sys.argv[3], sys.argv[4])
    else:
        print("Invalid command!")

if __name__ == "__main__":
    main()
