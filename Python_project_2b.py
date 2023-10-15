import os

def file_dict(path='.'):
    
    file_info = []

    for root, subdir, files in os.walk(path):
        for file in files:
            file_path = os.path.join(root, file)
            file_stat = os.stat(file_path)
            file_info.append({'Filename': file_path, 'Size(bytes)': file_stat.st_size})
    return file_info