import pyzipper
import sys

def crack_zip_password(zip_file):
    with pyzipper.AESZipFile(zip_file, 'r') as zipf:
        for i in range(0, 1000):  
            password = f"{i:03d}"  
            
            try:
                zipf.pwd = bytes(password, 'utf-8')
                zipf.extractall()  
                print(f"Password found: {password}")
                return
            except (RuntimeError, pyzipper.zipfile.BadZipFile, pyzipper.zipfile.LargeZipFile):
                # Wrong password, or the ZIP file is corrupted
                continue


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python cracking_encrypted_zip.py <zip_file_to_crack>")
        sys.exit()

    zip_file = sys.argv[1]
    crack_zip_password(zip_file)