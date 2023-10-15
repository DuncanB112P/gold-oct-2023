import os

# Define a function named 'file_dict' that generates a list of dictionaries with file information.
# The 'path' parameter is optional and defaults to the current directory ('.').
def file_dict(path='.'):
    # Create an empty list to store file information dictionaries.
    file_info = []

    # Use os.walk to traverse the directory tree starting from the specified 'path' (or current directory by default).
    for root, subdir, files in os.walk(path):
        # Iterate through the list of files in the current directory.
        for file in files:
            # Construct the full file path by joining the root directory and the current file name.
            file_path = os.path.join(root, file)
            # Get file statistics using os.stat to retrieve file size in bytes.
            file_stat = os.stat(file_path)
            # Create a dictionary for each file with 'Filename' and 'Size(bytes)' as keys.
            # 'Filename' stores the full path of the file, and 'Size(bytes)' stores its size.
            file_info.append({'Filename': file_path, 'Size(bytes)': file_stat.st_size})
    
    # Return the list of file information dictionaries.
    return file_info