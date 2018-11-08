import os

count = 0

os.system('cls')
print("what do you want to do?\n|___help :: Show help message\n|___start :: Start counting\n|___about :: Show about we\n==>")
command = input()
if command == "start":
  while True:
    os.system('cls')
    print (count)
    count += 1
    stop = input()
    if stop != "":
      break    
if command == "help":
    os.system('cls')
    print ("use Ctrl + C to stop")
if command == "about":
    os.system('cls')
    print ("Developer: Scorpion_Rn \nTelegram channel: \nGithub: \nSite: ")
