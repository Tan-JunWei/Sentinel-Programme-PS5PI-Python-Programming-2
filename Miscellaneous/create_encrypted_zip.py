import pyzipper
import sys

def create_encrypted_zip(file_to_zip, zip_file_name, password):
    with pyzipper.AESZipFile(zip_file_name,
                             'w',
                             compression=pyzipper.ZIP_DEFLATED,
                             encryption=pyzipper.WZ_AES) as zipf:
        zipf.setpassword(bytes(password, 'utf-8'))
        zipf.write(file_to_zip, arcname=file_to_zip.split('/')[-1])  # Ensuring only the file name is used in the archive

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: script.py <file_to_zip> <password>")
        sys.exit(1)

    file_to_zip = sys.argv[1]
    password = sys.argv[2]
    zip_file_name = f"{file_to_zip}.zip"

    create_encrypted_zip(file_to_zip, zip_file_name, password)
    print(f"Created encrypted {zip_file_name} with ZIP_DEFLATED compression")
