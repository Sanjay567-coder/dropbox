import dropbox
import os


class TransferData:
    def __init__(self, access_token):
        self.aT = access_token

    def upload_file(self, file_from, file_to):
        dbx = dropbox.Dropbox(self.access_token)
        fileName = os.path.split(file_from)[1]

        dropbox_file = '/CloudStorage/'+fileName

        with open(file_from, "rb") as f:
            dbx.files_upload(f.read(), dropbox_file,
                            mode=dropbox.files.WriteMode.overwrite)

def main():
    
    AToken = "sl.Av__rRKxl7D6OB63anvJVW6W-WP5NSQpiSUneoAmA3VoCBPjIDUAfTgMs-ap7wTU2iu0qKuhRo56N2Ca3SMQzlbu3OCQU7PQPBVSGUlZigLppSoouhGu7I0ep-FgM-G8EyMy-ug"

    cloudStoring = TransferData(access_token)

    while(os.path.isfile(file_from) == False):
        fileFrom = input("Enter the file path to transfer:- ")

    cloudStoring.upload_file(fileFrom)

    print("File had been moved!)")

if __name__ == '__main__':
    main() 
