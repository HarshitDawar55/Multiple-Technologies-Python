import os
import sys


def RunCommand(cmd):
    print(os.system(cmd))


def configure_docker():
    os.system("cd /etc/yum.repos.d")
    file_object = open("docker.repo", "w+")
    configs = ["name=Docker Configuration Repository", "baseurl=https://dl.fedoraproject.org/pub/epel/7/x86_64/", "gpgcheck=0"]
    file_object.writelines(configs)
    os.system("yum clean all")
    os.system("dnf install -y docker-ce --nobest")
    os.system("systemctl start docker --now")


def SpecificCommands():
    print("""Functionality supported by this software are listed below:
    Press 1 to check Date
    Press 2 to check Calender
    Press 3 to create a Directory
    Press 4 to create a File
    Press 5 to Enter Data into a file
    Press 6 to move a file
    Press 7 to check the OS Details
    Press 8 to check the IP of the System
    Press 9 to list the contents of a directory
    Press 10 to see the content of a file
    Press 11 to ping to a website
    Press 12 to add a user in the system
    Press 13 to remove a user
    Press 14 to list the mounted partitions
    Press 15 to list all the block partitions
    Press 16 to configure Docker""")

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
    elif ch == 8:
        print("Enter 1 if you are Virtual Machine else Press 2\n")
        option = int(input())
        if option == 1:
            print(os.system("ifconfig enp0s3 | grep inet* | head -n +1 | cut -c 14-25"))
        elif option == 2:
            print(os.system("ifconfig eth0 | grep inet* | head -n +1 | cut -c 14-25"))
        else:
            print("Incorrect Option, Exiting!!!")
    elif ch == 9:
        path = input("Enter the path of the Directory!\n")
        print(os.system("ls -lah {}".format(path)))
    elif ch == 10:
        path = input("Enter the path of the file!\n")
        print(os.system("cat {}".format(path)))
    elif ch == 11:
        url = input("Enter the URL of the website!\n")
        print(os.system("ping {}".format(url)))
    elif ch == 12:
        username = input("Enter the name of the user to add!\n")
        os.system("useradd {}".format(username))
    elif ch == 13:
        username = input("Enter the name of the user to delete!\n")
        os.system("userdel {}".format(username))
    elif ch == 14:
        os.system("df -h")
    elif ch == 15:
        os.system("lsblk")
    elif ch == 16:
        configure_docker()
    else:
        print("Wrong Input! Exiting!!!")
        sys.exit(0)


print(""""//////////////////////////////Important Note: This program is best supported on OS based on CentOS//////////////////////////""")
while True:
    print(" Press 1: To Run Command Locally!\n Press 2: To run Command Remotely!\n Press 3 To exit from the Program!\n")
    choice = int(input())

    if choice == 1:
        print("Press 1 to run any command!\nPress 2 to use the functionality supported by this software!\n")
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

