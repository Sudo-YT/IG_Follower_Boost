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
                                                        
{}\n\t[+] Welcome To Sudos's Instagram Follower Booster (•◡ •) /\n\t[+] Subscribe To Sudo On YT\n\t[+] NOTE: Make Sure You Have Firefox Installed And 2FA Is Off\n{}""".format("="*100,"="*100,"="*100))

user = input("[+] Enter you username: ")
pw = getpass.getpass("[+] Enter you user password: ")
fol = input("[+] Would you like to follow these accounts? (y/n): ")
follow = input("[+] Enter the max amount of people to want to follow: ")

session = InstaPy(username=user, password=pw)
session.login()

session.set_relationship_bounds(enabled=True, max_followers=int(follow))

if fol == "y":
    session.set_do_follow(True, percentage=100)
if fol == "n":
    session.set_do_follow(True, percentage=0)

session.like_by_tags(["love", "photography", "travel"], amount=4) # Add tags here and when you do add all the tags together and add one to amount
session.set_dont_like("nsfw")

session.end()