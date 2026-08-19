import os
import shutil

def move_jpg_files(source_dir, destination_dir):
    """Automates moving all .jpg files from a source folder to a destination folder."""
    if not os.path.exists(source_dir):
        print(f"Source folder '{source_dir}' does not exist.")
        return

    # Create destination directory if it doesn't exist
    if not os.path.exists(destination_dir):
        os.makedirs(destination_dir)
        print(f"Created directory: {destination_dir}")

    moved_count = 0
    for filename in os.listdir(source_dir):
        if filename.lower().endswith(".jpg") or filename.lower().endswith(".jpeg"):
            src_path = os.path.join(source_dir, filename)
            dest_path = os.path.join(destination_dir, filename)
            
            shutil.move(src_path, dest_path)
            print(f"Moved: {filename}")
            moved_count += 1

    print(f"\nAutomation Complete! Total .jpg files moved: {moved_count}")

if __name__ == "__main__":
    print("=== File Automation: Move JPG Files ===")
    src = input("Enter source directory path (e.g., ./my_folder): ").strip()
    dest = input("Enter destination directory path (e.g., ./jpg_folder): ").strip()
    
    if src and dest:
        move_jpg_files(src, dest)
    else:
        print("Paths cannot be empty.")