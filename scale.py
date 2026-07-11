user_answer = input("What is your weight?")

user_weight = user_answer.replace(" ", "")

weight_measure = input("In (K)gs or (L)bs?")
weight_measurem = weight_measure.lower()
weight_measurment = weight_measurem.replace(" ", "")

if weight_measurment == "k":
    print( "Your weight is " + str(int(user_weight) * 2.2046) + " in lbs")
elif weight_measurment == "l":
    print( "Your weight is " + str(int(user_weight) * 2.2046) + " in kgs")
