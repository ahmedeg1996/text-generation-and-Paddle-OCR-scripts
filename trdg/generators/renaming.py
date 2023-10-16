import os

path = '/path/to/directory'  # Replace with the path to your directory

files = os.listdir(path)
num_files = len(files)

for i, file_name in enumerate(files):
    _, ext = os.path.splitext(file_name)
    new_file_name = f"{i+1000:04d}{ext}"
    os.rename(os.path.join(path, file_name), os.path.join(path, new_file_name))

