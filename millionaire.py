#!usr/bin/python3
import random

f = open("questions.txt")
questions = f.readlines()
f.close()
tp = open("top_players.txt")
players = tp.readlines()
tp.close()

print("Players")
for i in range(len(players)):
    players[i] = players[i][0:len(players[i])-1].split()
    print(*players[i])

for i in range(len(questions)):
    questions[i] = questions[i][0:len(questions[i])-1]
    print(questions[i])

def verifying(name,ml):
    for i in ml:
        if i[0] == name:
            print("Do you want to overwrite your results?")
            answer = input()
            if answer.lower() == "yes":
                print("Okay")
                ml.pop(i)
                break
            username = input("Enter another username")
            verifying(username,ml)

game_questions = []

while len(game_questions) < 10:
    num = random.randint(0, len(questions)-1)
    if questions[num] not in game_questions:
        game_questions.append(questions[num])

gquestions = {}
for el in game_questions:
    q,a = el.split("?")
    gquestions[q] = a.split(",")

username = input("Enter your username: ")
verifying(username,players)

cnt = 0
variant = ["A", "B", "C", "D"]
cvariant = ""
for q,a in gquestions.items():
    print(q)
    correct = a[0]
    random.shuffle(a)
    for i in range(len(variant)):
        print(variant[i], a[i])
        if a[i] == correct:
            cvariant = variant[i]
    answer = input("Your variant: ")
    if answer.upper() == cvariant:
        cnt += 1
        print("Correct.")
    else:
        print("Not. Correct answer was: ", correct)

print("You got %d/10" %cnt)
players.append([username,str(cnt)])
n = len(players)
for i in range(n):
	for j in range(0, n-i-1):
		if int(players[j][1]) < int(players[j+1][1]):
			players[j], players[j+1] = players[j+1], players[j]
for i in range(len(players)):
    players[i] = ' '.join(players[i])+'\n'
print(players)
f  = open("top_players.txt","w")
for i in players:
    f.write(i)
f.close()
