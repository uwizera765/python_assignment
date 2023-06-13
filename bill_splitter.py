#name: Irakiza Uwizera Oliva
#reg: 221021376
#IT department
import  random
friends_joining_dinner_party = {}
friends_no = int(input("enter the number of friends (including you):\n"))
if (friends_no <= 0):
    print("No one is joining for the party")
else:
    print("enter names of friends(including you)")
    for friend in range(friends_no):
        friend_name = input()
        friends_joining_dinner_party.update({friend_name: 0})
    total_bill = int(input("enter the total_bill: \n"))
    splitted_bill=total_bill/friends_no
    friends_joining_dinner_party = {c: round(splitted_bill, 2) for c in friends_joining_dinner_party}
    print(friends_joining_dinner_party)
    file = input()
    if file == 'Yes':
        file= random.choice(list(friends_joining_dinner_party))
        print("%s is the lucky one!"%file)
        friends_joining_dinner_party = {c: (total_bill)/(friends_no-1) for c in friends_joining_dinner_party}
        friends_joining_dinner_party.update({file:0})
        print(friends_joining_dinner_party)
    elif  file == 'No':
        print("No one is going to be lucky")
        print()
        print(friends_joining_dinner_party)
    else:
        print("invalid input")