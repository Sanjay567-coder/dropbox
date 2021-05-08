import os
import dropbox

class TransferData:
    def __init__(self, access_token):
        self.atoken = access_token

    def upload_file(self, file_from, file_to):
        dbx = dropbox.Dropbox(self.atoken)

        for root,dirs,files in os.walk(file_from):
            for fileName in files:
                localpath = os.path.join(root,fileName)
                relativepath = os.path.relpath(localpath,file_from)
                dropboxpath = os.path.join(file_to,relativepath)

                with open(localpath, "rb") as f:
                    dbx.files_upload(f.read(), dropboxpath,
                            mode=WriteMode('overwrite'))

def main():
    
    AToken = "sl.AwIeDKcJc1TG4rF8djcnjoif99W8NfnMHAPlPmRizJg0iFV8W3I06MPbzdyvElxBpE77CSf56f7fuKG1R3UJAlqqampYw-q68AqKA64CUCoa0MVrDBhnXrYRX7_QgGI0PsgQ-mQw"

    cloudStoring = TransferData(AToken)

    fileFrom = input("Enter the file path to transfer:- ")

    fileTo = input("Enter the file path to upload to dropbox:- ")

    cloudStoring.upload_file(fileFrom, fileTo)

    print("File had been moved!)")

if __name__ == '__main__':
    main() 
