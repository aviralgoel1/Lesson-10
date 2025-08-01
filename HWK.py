import os
command=input("Do you want to shutdown?")
if command == "yes":
    os.system("shutdown /p")
else:
    print ("Will not shutdown")