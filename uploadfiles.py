import dropbox
import os
from dropbox.files import WriteMode

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        """upload a file to Dropbox using API v2
        """
        dbx = dropbox.Dropbox(self.access_token)
        
        for root,dirs,files in os.walk(file_from):
            for filename in files :
                local_path=os.path.join(root,filename)
                relative_path=os.path.relpath(local_path,file_from)
                dropbox_path=os.path.join(file_to,relative_path)
        

                with open(local_path, 'rb') as f:
                    dbx.files_upload(f.read(), dropbox_path,mode=WriteMode('overwrite'))

def main():
    access_token = 'sl.BJo_A-WhZX8Tht5aeHOjW9kNK1IzmFJIVzAEayfvxF0sRPVXm6wi96jlc6HztS8lbnuorHjeA8EOrQxHQn_lqSaW9HBPEt7aqPv-esbF0rgn3uIJ6xYJ6xCKVQCxBREbx6mg-vJEE_1E'
    transferData = TransferData(access_token)

    #file_from = 'test.txt'
    #file_to = '/test_dropbox/test.txt'  # The full path to upload the file to, including the file name

    file_from=input("Enter the file to transfer: ")
    file_to = input("Enter the path to upload: ")

    # API v2
    transferData.upload_file(file_from, file_to)

if __name__ == '__main__':
    main()
 