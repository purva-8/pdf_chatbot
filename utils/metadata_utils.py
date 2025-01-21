import json
import os

# Function to load metadata from a file
def load_metadata(file_path):
    metadata = {}
    if os.path.exists(file_path) and os.path.getsize(file_path) > 0:
        try:
            with open(file_path, "r") as f:
                metadata = json.load(f)  # Load the JSON content
        except json.JSONDecodeError:
            # If JSON decoding fails, log a warning and reset the metadata
            print("Warning: Metadata file is corrupted. Resetting...")
            metadata = {}
    else:
        print("Metadata file not found or is empty.")
    
    return metadata

def save_metadata_safely(pdf_id, pdf_data, file_path):
    """
    Save metadata in a JSON file with proper formatting and line breaks for readability.
    """
    # Load existing metadata
    metadata = load_metadata(file_path)

    # Update metadata with the new PDF data
    metadata[pdf_id] = pdf_data

    # Save metadata back to the file with formatting
    with open(file_path, "w") as f:
        json.dump(metadata, f, indent=4)  # Save with indentation (adds line breaks)

