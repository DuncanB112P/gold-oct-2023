import os

# Define a function named 'file_dict' that generates a list of dictionaries containing file information.
# The 'path' parameter is optional and defaults to the current directory ('.').
def file_dict(path='.'):
    # Create an empty list to store dictionaries with file information.
    file_info = []

    # Use os.walk to recursively traverse the directory tree starting from the specified 'path' (or the current directory by default).
    for root, dirs, files in os.walk(path):
        # Iterate through the list of files in the current directory.
        for file in files:
            # Construct the full file path by joining the root directory and the current file name.
            file_path = os.path.join(root, file)
            # Get file statistics using os.stat to retrieve file size in bytes.
            file_stat = os.stat(file_path)
            # Create a dictionary for each file with 'FILENAME' and 'SIZE(bytes)' as keys.
            # 'FILENAME' stores the full path of the file, and 'SIZE(bytes)' stores its size in bytes.
            file_data = {
                'FILENAME': file_path,
                'SIZE(bytes)': .st_size
            }
            # Append the file data dictionary to the 'file_info' list.
            file_info.append(file_data)
    
    # Print the file information in the list, with each file's data separated by a newline character.
    print(*file_info, sep='\n')

# Call the 'file_dict' function with the default path (current directory).
file_dict()