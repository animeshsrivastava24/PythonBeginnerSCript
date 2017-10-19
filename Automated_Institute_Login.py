#This Code Snippet can be used to login Automatically into any website(preferably a frequently used Website that requires your login credentials everytime you Turn your PC ON).The code uses splinter to perform the same. Just modify your Username and Password and Run the .py file ,Sit back and relax!!!.  
 
from splinter.browser import Browser
from time import sleep
 
URL = 'https://controller.mobile.lan/103/portal/'
NAME = 'login_name'
PASSWORD = 'login_password'
 
def main():
    br = Browser('chrome') #The Browser function takes the "Browser name" as an argument, it can be changed as per will.
    br.visit(URL)
    sleep(3)
    if br.is_text_present('Connection', wait_time=7):
        br.fill('login', NAME)
        br.fill('password', PASSWORD)
        br.find_by_css('#logonForm_connect_button').first.click()
 
#############################################################################
 
if __name__ == "__main__":
    main()
