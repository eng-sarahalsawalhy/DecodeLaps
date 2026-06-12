

print("------welcome to Sarah's ChatBot! :)------")

while True:
    
    user_ip = input("User: ").lower().strip()

    # loop

    # greeting
    if user_ip in ["hi","hello","hey"]:
        print("SBot: Hello!")

    # asking the bot how is it
    elif user_ip in ["how are you","how are you?"]:
        print("SBot: I'm fine ,thanks!")
    
    # asking about its name
    elif user_ip=="what's your name?":
        print("SBot: I'm sarah's AI chatbot")

    # exit chat
    elif user_ip in["exit","bye","end"]:
        print("SBot: ok bye! :(")
        break

    # if i type any other input
    else:
        print("SBot:sorry! can't understand you :/")


