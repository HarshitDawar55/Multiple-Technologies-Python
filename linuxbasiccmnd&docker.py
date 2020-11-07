import os
import sys


def RunCommand(cmd):
    print(os.system(cmd))


def SpecificCommands():
    print("""Functionalities supported by this software are listed below:\n
           Press 1 to check Date\n
           Press 2 to check Calender\n
           Press 3 to create a Directory\n
           Press 4 to create a File\n
           Press 5 to Enter Data into a file\n
           Press 6 to move a file\n
           Press 7 to check the OS Details\n
           Press 8 to check the IP of the System\n
           Press 9 to list the contents of a directory\n
           Press 10 to see the content of a file\n
           Press 11 to ping to a website\n
           Press 12 to add a user in the system\n
           Press 13 to remove a user\n
           Press 14 to list the mounted partitions\n
           Press 15 to list all the block partitions\n""")
    ch = int(input())

    if ch == 1:
        print(os.system("date"))
    elif ch == 2:
        print(os.system("cal"))
    elif ch == 3:
        path = input("Enter the path where the directory has to be created!\n")
        os.system("mkdir -p {}".format(path))
    elif ch == 4:
        path = input("Enter the path with file name where the file has to be created!\n")
        os.system("touch {}".format(path))
    elif ch == 5:
        path = input("Enter the path of the file!\n")
        data = input("Enter the data to be inserted!\n")
        fileObject = open("{}".format(path), "a+")
        fileObject.writelines(data)
    elif ch == 6:
        initialPath, FinalPath = input(
            "Enter the file path where the file is present & the path where it has to be moved(space separated)!\n").split()
        os.system("mv {} {}".format(initialPath, FinalPath))
    elif ch == 7:
        print(os.system("cat /etc/os-release"))


while True:
    print("""//////////////////////////////////////////////Important Note: This program is best supported on OS based on CentOS//////////////////////////////////////////////\n
     Press 1: To Run Command Locally!\nPress 2: To run Command Remotely!\n Press 3 To exit from the Program!\n""")
    choice = int(input())

    if choice == 1:
        print("Press 1 to run any command!\nPress 2 to use the functionalities supported by this software!\n")
        ch = int(input())
        if ch == 1:
            try:
                cmd = input("Enter the Command!")
                RunCommand(cmd)
            except Exception:
                print(Exception)

        if ch == 2:
            try:
                SpecificCommands()
            except Exception:
                print(Exception)

    elif choice == 3:
        sys.exit(1)
    else:
        print("Wrong Option!")

    '''def linxcmnd():
        if int(channel) == 1:
            os.system("clear")
            print("			Linux Commands			")
            print("""\n
			Press 1: To run Date
			Press 2: To run Calender
			Press 4: To know the host/network
			Press 5: To create new blank file in linux 
			Press 6: To check connectivity status 
			Press 7: To Add a new user
			Press 8: To remove a user
			Press 9: To make a new Directory
			Press 0: To Exit

			""")

            x = input("Enter your Choice: ")
            print(x)

            if int(x) == 1:
                os.system("date")

            elif int(x) == 2:
                os.system("cal")

            elif int(x) == 3:
                os.system("ifconfig")

            elif int(x) == 4:
                os.system("hostname -I")

            elif int(x) == 5:
                File_name = input("Enter the filename you want to create: ")
                os.system("touch {0}".format(File_name))

            elif int(x) == 6:
                os.system("ping")

            elif int(x) == 7:
                user_name = input("Enter the User name you want to Add: ")
                os.system("useradd {0}".format(user_name))
                os.system("getent passwd | grep {0}".format(user_name))
                print("User Added")

            elif int(x) == 8:
                user_name = input("Enter the User namee you want to Delete: ")
                os.system("userdel {0}".format(user_name))
                print("User Deleted")

            elif int(x) == 9:
                dir_name = input("Enter the Directory name you want to create: ")
                os.system("mkdir {0}".format(dir_name))

            elif int(x) == 0:
                os.system("exit")

        linxcmnd()'''


    def docker():
        if int(channel) == 2:
            os.system("clear")
            print("			Let us Configure Docker 			")
            print("""\n
			For Configuring DOCKER press the following option stepwise...
			Press 1: Configure yum for Docker 
			Press 2: To install Docker 
			Press 3: To start Docker services 
			Press 4: To check docker status if running
			Press 0: To Exit
			""")

            x = input("Enter your Choice: ")
            print(x)
            if int(x) == 1:
                dock_repo = input("Enter docker repository : ")
                os.system("cp {0} /etc/yum.repos.d".format(dock_repo))
                os.system("yum repolist")
                print("Repolist Checked ")
                os.system("yum list docker -ce")

            elif int(x) == 2:
                os.system("yum install docker -ce --nobest")

            elif int(x) == 3:
                os.system("rpm -q docker -ce")
                os.system("systemctl start docker")
                print("Docker service started..")

            elif int(x) == 4:
                os.system("systemctl status docker")
                print("Now you install container-O.S .")
        docker()

input("\nPlease Enter to Contiune..")
