import os

def print_directory_contents(path):
    try:
        # Get the list of all files and directories in the specified path
        contents = os.listdir(path)
        
        print(f"Contents of directory '{path}':")
        for item in contents:
            print(item)
    except FileNotFoundError:
        print(f"The directory '{path}' does not exist.")
    except PermissionError:
        print(f"Permission denied to access the directory '{path}'.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Specify the path of the directory you want to list
directory_path = "/"

# Call the function
print_directory_contents(directory_path)
