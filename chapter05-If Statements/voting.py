age = 16

if age >= 18:
    print("You are old enough to vote!")
    print("Have you registered to vote yet?")
if age < 18:
    print("You are too young to vote at {}. You have another {} years to wait.".format(age ,18-age))
