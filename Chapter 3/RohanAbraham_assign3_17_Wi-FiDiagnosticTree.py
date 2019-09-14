#Rohan Abraham
#Program will act as a Wi-Fi diagnostic tool.

print("Reboot the router and try to connect")
clarify = "Did that fix the problem? "

prompt = input(clarify)
if(prompt == "yes"):
    print("")
else:
    print("Reboot the router and try to connect.")
    prompt1 = input(clarify)
    if(prompt1 == "yes"):
        print("")
    else:
        print("Make sure the cable betweent the router and the motem are plugged in firmly.")
        prompt2 = input(clarify)
        if(prompt2 == "yes"):
            print("")
        else:
            print("Move the router to a new location and try to connect.")
            prompt3 = input(clarify)
            if(prompt3 == "yes"):
                print("")
            else:
                print("Get a new router.")
        
            
