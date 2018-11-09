import os

count = 0

def clear():
    c = { "linux":"clear" , "win":"cls"}
    if os.name != "nt":
        os.system(c["linux"])
    else:
        os.system(c["win"])
    return
	
clear()
print("what do you want to do?\n|___help :: Show help message\n|___start :: Start counting\n|___about :: Show about we\n==>")
command = input()
if command == "start":
  while True:
    clear()
    print (count)
    count += 1
    stop = input()
    if stop != "":
      break    
if command == "help":
    clear()
    print ("use Ctrl + C to stop")
if command == "about":
    clear()
    print ("Developer: Scorpion_Rn \nTelegram channel: \nGithub: \nSite: ")
