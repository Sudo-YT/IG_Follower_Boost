# Coded by Sudo
import getpass
from instapy import InstaPy

print("\033[1;32;40m\n""""{}
 _______  __   __  ______   _______  _______                                              
|       ||  | |  ||      | |       ||       |                                             
|  _____||  | |  ||  _    ||   _   ||  _____|                                             
| |_____ |  |_|  || | |   ||  | |  || |_____                                              
|_____  ||       || |_|   ||  |_|  ||_____  |                                             
 _____| ||       ||       ||       | _____| |                                             
|_______||_______||______| |_______||_______|                                             
 ___   _______    _______  _______  ___      ___      _______  _     _  _______  ______   
|   | |       |  |       ||       ||   |    |   |    |       || | _ | ||       ||    _ |  
|   | |    ___|  |    ___||   _   ||   |    |   |    |   _   || || || ||    ___||   | ||  
|   | |   | __   |   |___ |  | |  ||   |    |   |    |  | |  ||       ||   |___ |   |_||_ 
|   | |   ||  |  |    ___||  |_|  ||   |___ |   |___ |  |_|  ||       ||    ___||    __  |
|   | |   |_| |  |   |    |       ||       ||       ||       ||   _   ||   |___ |   |  | |
|___| |_______|  |___|    |_______||_______||_______||_______||__| |__||_______||___|  |_|
 _______  _______  _______  _______  _______  _______  ______                             
|  _    ||       ||       ||       ||       ||       ||    _ |                            
| |_|   ||   _   ||   _   ||  _____||_     _||    ___||   | ||                            
|       ||  | |  ||  | |  || |_____   |   |  |   |___ |   |_||_                           
|  _   | |  |_|  ||  |_|  ||_____  |  |   |  |    ___||    __  |                          
| |_|   ||       ||       | _____| |  |   |  |   |___ |   |  | |                          
|_______||_______||_______||_______|  |___|  |_______||___|  |_|                          
                                                        
{}\n\t[+] Welcome To Sudo's Instagram Follower Booster (•◡ •) /\n\t[+] Subscribe To Sudo On YT\n\t[+] NOTE: Make Sure You Have Firefox Installed And 2FA Is Off\n{}""".format("="*100,"="*100,"="*100))

user = input("[+] Enter you username: ")
pw = getpass.getpass("[+] Enter you user password: ")
like = input("[+] What tag do you want to search?: ")
view = input("[+] How many posts do you want to view?: ")
fol = input("[+] Do you want to follow these accounts? (y/n): ")
com = input("[+] Do you want to comment on these posts? (y/n): ")

session = InstaPy(username=user, password=pw)
session.login()

session.set_relationship_bounds(enabled=True, max_followers=int(view))

session.like_by_tags([like], amount=2)

if fol == "y":
    session.set_do_follow(True, percentage=100)
if fol == "n":
    session.set_do_follow(False, percentage=0)

if com == "y":
    session.set_do_comment(enabled=True, percentage=100)
    session.set_comments(["Amazing!", "Nice", "Great stuff"])
if com == "n":
    session.set_do_comment(enabled=False, percentage=0)

session.set_dont_like(["1", "2"]) # Add tags to 100% avoid here

session.end()
