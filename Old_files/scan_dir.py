import os.path
for current_dir, dirs, files in os.walk(".."):
    print(current_dir, dirs, files)