import zipfile
import os

def zip_folder(folder_path, output_zip_path):
    print(f"hihihiHahahaha1111 {folder_path, output_zip_path}")
    with zipfile.ZipFile(output_zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
        print(f"hihihiHahahaha {folder_path, output_zip_path}")
        for root, _, files in os.walk(folder_path):
            for file in files:
                print(f"hihihi {root,folder_path, output_zip_path}")
                abs_path = os.path.join(root, file)
                rel_path = os.path.relpath(abs_path, folder_path)
                zipf.write(abs_path, rel_path)