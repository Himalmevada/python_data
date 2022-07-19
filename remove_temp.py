# for i in os.listdir():
import os

path = os.chdir("c:\\Windows\\Temp")
# path = os.chdir("c:\\Users\\mevad\\AppData\\Local\\Temp")


for i in os.scandir(path):
    if i.is_file():
        try:
            os.remove(i)
            print(f"{i.name} has been removed")
        except Exception as err:
            print('Error',err)
    else:
        if i.is_dir():
            try:
                os.rmdir(i)
                print(f"{i.name} has been removed")
            except Exception as err:
                print('Error',err)
