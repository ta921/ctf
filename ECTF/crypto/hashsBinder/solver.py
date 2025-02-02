import io
import msoffcrypto
#import openpyxl as excel

filePass = 'parts.xlsx'
paswardListFile = open('wordlists.txt', 'r')

password = paswardListFile.readline()

decrypted = io.BytesIO()
with open(filePass, 'rb') as fp:
    msfile = msoffcrypto.OfficeFile(fp)
    msfile.load_key(password=password)
    msfile.decrypt(decrypted)

print(decrypted.getbuffer())

