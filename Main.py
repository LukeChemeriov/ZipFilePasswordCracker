'''imports'''
import zipfile


count = 1

print("Enter name of zip file (include zip extension):")
name = input()
def testPassword(passwordlist, filename):
    with open(passwordlist,'rb') as text:
         for entry in text.readlines():
            password = entry.strip()
            try:
                with zipfile.ZipFile(filename,'r') as zf:
                    zf.extractall(pwd=password)

                    data = zf.namelist()[0]

                    data_size = zf.getinfo(data).file_size
 
                    print('''******************************\n[+] Password found! ~ %s\n ~%s\n ~%s\n******************************''' 
                        % (password.decode('utf8'), data, data_size))
                    cracked = true
                    break

            except:
                number = count
                print('[%s] [-] Password failed! - %s' % (number,password.decode('utf8')))
                count += 1
                pass
                cracked = false
testPassword("passwords.txt")
if (cracked == true):
    exit(0)
else:
    print("Password could not be found. Do you wish to try again with a different dictionary?")
    confirmyn = input().lower()
    if (confirmyn == "y"):
        testPassword("passwords2.txt")
    else:
        exit/(-1)
       
