'''
This is the frontend of our menu program
'''

from colorama import init
import termcolor as tc

#importing packages
from colorama import init
import termcolor as tc
import someFunctions as sf
#initialise the colorama for use with termcolor
init() 
print(tc.colored("\t\t\t\t************************", color='green', attrs=['blink']))
print(tc.colored("\t\t\t\t*                      *",color='green', attrs=['blink']))
print(tc.colored("\t\t\t\t* ",color='green', attrs=['blink']), end='')
print(tc.colored(" ", "green", on_color='on_white',attrs=['bold',]),end='')
print(tc.colored("Welcome To WoW Menu", "green", on_color='on_white',attrs=['bold',]),end='')
print(tc.colored(" *",color='green', attrs=['blink']))
print(tc.colored("\t\t\t\t*                      *",color='green', attrs=['blink']))
print(tc.colored("\t\t\t\t*************************",color='green', attrs=['blink']))


def display_menu():
    """
    This function will display the menu to the user
    """
    menu = ''' 
    1.  print date
    2.  print calender
    3.  check webserver status
    4.  install webserver
    5.  install a package
    6.  start, stop or reload a service
    7.  configure yum
    8.  create a directory
    9.  create a user
    10. Launch ec2-instance and configure webserver on top of it
    11. Setup hadoop master and worker nodes
    12. Install docker on redhat
    13. exit
    '''
    print(tc.colored(menu, color='green', attrs=['bold']))
if __name__ == '__main__':
    #This will run the full program
    while True:
        display_menu()
        print(tc.colored("Enter choice: ", 'green', attrs=['bold']), end='')
        ch = input()
        if ch == '1':
            sf.date()
        elif ch == '2':
            sf.calender()
        elif ch == '3':
            print(tc.colored("Do you want to run in localhost or remote ip:", 'green', attrs=['bold']), end=' ')
            choice = input()
            if choice == 'localhost':
                sf.webserver_status()
            else:
                sf.webserver_status_remote()
        elif ch == '4':
            print(tc.colored("Do you want to run in localhost or remote ip:", 'green', attrs=['bold']), end=' ')
            choice = input()
            if choice == 'localhost':
                sf.webserver_install()
            else:
                ip = input(tc.colored("Enter remote ip: ", 'green', attrs=['bold']))
                sf.webserver_install_remote(ip)
        elif ch == '5':
            sf.install_pkg()
        elif ch == '6':
            sf.service()
        elif ch == '7':
            sf.yum_config()
        elif ch == '8':
            sf.create_dir()
        elif ch == '9':
            sf.create_user()
        elif ch == '10':
            sf.launch_ec2_instance()
        elif ch == '11':
            sf.hadoop()
        elif ch == '12':
            sf.docker()
        elif ch == '13':
            print(tc.colored("See you next time :)", color='green', attrs=['bold']))
            break
        else:
            print(tc.colored("Wrong Input!!!", color='red', attrs=['bold']))
