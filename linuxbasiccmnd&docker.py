import os

print("Press 1: To Run Command Locally\nPress 2: To run Command Remotely")

choice = input("Enter your Choice: ")
while True:
    def linxcmnd():
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

        linxcmnd()


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
