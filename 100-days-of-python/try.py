import random

random_ans = ["Yes - definitely", 
              "It is decidedly so",
              "Without a doubt",
              "Reply hazy, try again",
              "Ask again later",
              "Better not tell you now",
              "My sources say no",
              "Outlook not so good",
              "Very doubtful"]

random_num = random.randint(1 , len(random_ans))


print("Answerable by yes or no questions Only !")
name = input("What is your name?: ")
question = input("What is your Question?: ")

print (name, " asks:  ", question )
print("Magic 8-ball's answer: ", random_ans[random_num])