import os

# Ensure directories exist
def ensure_directory_exists(path):
    if not os.path.exists(path):
        os.makedirs(path)
