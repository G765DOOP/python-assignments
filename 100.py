 #Calender?



date = str(input("What day would you like to set?     (mm/dd/yyyy)"))
remove_0 = "0"
event = str(input("What's the occasion?"))

date2 = date.replace(remove_0, "")

#now asking abt calender

ask_day = str(input("What day do you want to ask about? (mm/dd/yyyy)"))

ask_day2 = ask_day.replace(remove_0, "")

if ask_day2 == date2:
    print("You have" + event + "!")


