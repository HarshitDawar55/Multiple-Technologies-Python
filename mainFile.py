import os
import sys


def print_success():
    print("////////////////////Operation Completed Successfully////////////////////")


def RunCommand(cmd):
    print(os.system(cmd))


def configure_docker():
    os.system("yum clean all")
    os.system("yum repolist")
    os.system("cd /etc/yum.repos.d/")
    file_object = open("docker.repo", "w+")
    configs = ["[docker-repo]\n", "name=Docker Configuration Repository\n",
               "baseurl=https://download.docker.com/linux/centos/7/x86_64/stable/\n", "gpgcheck=0\n"]
    file_object.writelines(configs)
    print_success()


def install_docker():
    os.system("dnf install -y docker-ce --nobest")
    os.system("systemctl start docker --now")
    print_success()


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
    """)

    ch = int(input())

    if ch == 1:
        print(os.system("date"))
        print_success()
    elif ch == 2:
        print(os.system("cal"))
        print_success()
    elif ch == 3:
        path = input("Enter the path where the directory has to be created!\n")
        os.system("mkdir -p {}".format(path))
        print_success()
    elif ch == 4:
        path = input("Enter the path with file name where the file has to be created!\n")
        os.system("touch {}".format(path))
        print_success()
    elif ch == 5:
        path = input("Enter the path of the file!\n")
        data = input("Enter the data to be inserted!\n")
        fileObject = open("{}".format(path), "a+")
        fileObject.writelines(data)
        print_success()
    elif ch == 6:
        initialPath, FinalPath = input(
            "Enter the file path where the file is present & the path where it has to be moved(space separated)!\n").split()
        os.system("mv {} {}".format(initialPath, FinalPath))
        print_success()
    elif ch == 7:
        print(os.system("cat /etc/os-release"))
        print_success()
    elif ch == 8:
        print("Enter 1 if you are Virtual Machine else Press 2\n")
        option = int(input())
        if option == 1:
            print(os.system("ifconfig enp0s3 | grep inet* | head -n +1 | cut -c 14-25"))
            print_success()
        elif option == 2:
            print(os.system("ifconfig eth0 | grep inet* | head -n +1 | cut -c 14-25"))
            print_success()
        else:
            print("Incorrect Option, Exiting!!!")
    elif ch == 9:
        path = input("Enter the path of the Directory!\n")
        print(os.system("ls -lah {}".format(path)))
        print_success()
    elif ch == 10:
        path = input("Enter the path of the file!\n")
        print(os.system("cat {}".format(path)))
        print_success()
    elif ch == 11:
        url = input("Enter the URL of the website!\n")
        print(os.system("ping {}".format(url)))
        print_success()
    elif ch == 12:
        username = input("Enter the name of the user to add!\n")
        os.system("useradd {}".format(username))
        print_success()
    elif ch == 13:
        username = input("Enter the name of the user to delete!\n")
        os.system("userdel {}".format(username))
        print_success()
    elif ch == 14:
        os.system("df -h")
        print_success()
    elif ch == 15:
        os.system("lsblk")
        print_success()
    else:
        print("Wrong Input! Exiting!!!")
        sys.exit(0)


print(
    """"//////////////////////////////Important Note: This program is best supported on OS based on CentOS//////////////////////////""")
while True:
    print(" Press 1: To Run Command Locally!\n Press 2: To run Command Remotely!\n Press 3 To exit from the Program!\n")
    choice = int(input())

    if choice == 1:
        print("Press 1 to run any command!\nPress 2 to run the basic Linux Commands supported by this software!")
        print("Press 3 to configure Docker!\nPress 4 to install Docker!\n")
        ch = int(input())
        if ch == 1:
            try:
                cmd = input("Enter the Command!")
                RunCommand(cmd)
            except Exception:
                print(Exception)

        elif ch == 2:
            try:
                SpecificCommands()
            except Exception:
                print(Exception)

        elif ch == 3:
            try:
                configure_docker()
            except Exception:
                print(Exception)

        elif ch == 4:
            try:
                install_docker()
            except Exception:
                print(Exception)

        else:
            print("Wrong Output! Exiting!!!")
            sys.exit(0)

    elif choice == 3:
        sys.exit(1)
    else:
        print("Wrong Option!")
