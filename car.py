started = False
while True:
    command = input("> ")
    commandl = command.lower()
    
    if commandl == "help":
        print("start - to start the car")
        print("stop - to stop the car")
        print("quit - to quit the game")
        
    elif commandl == "start":

        if started:
            print("Car already started!")

        else:
            started = True
            print("Car started...Ready to go!")

    elif commandl == "stop":

        if not started:
            print("Car stopped already!")
        
        else:
            started = False
            print("Car stopped.")

    elif commandl == "quit":
        break
        
    else:
        print("I don't understand that")

 
 