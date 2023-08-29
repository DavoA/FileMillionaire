#!/usr/bin/python3

import random
import os.path
def adding_questions(fname):
    questions = get_questions_from_file(fname)
    only_questions = []
    for el in questions:
        only_questions.append(el.strip().split("?")[0]+"?")
    checking = input("Do you want to add more questions into the game y/n: ")
    while checking == "y":
        question = input("Write your question: ")
        while question in only_questions:
            question = input("This question allready exists in data\nWrite new question: ")
        correct = input("Enter the corect answer: ")
        options = input("Other 3 options: ").split()
        while len(options) != 3:
            options = input("You must put spaces between them: ").split()
        with open("questions.txt", "a") as f:
            f.write(question+correct+","+",".join(options)+"\n")
        checking = input("Do you want to add more questions into the game y/n: ")


def get_random_5_questions(questions):
	tmp = []
	while len(tmp) < 5:
		num = random.randint(0, len(questions) -1)
		if questions[num] not in tmp:
			tmp.append(questions[num])
	return tmp

def structure_questions(tmp):
	gquestions = {}

	for el in tmp:
		q, a = el.split("?")
		gquestions[q+"?"] = a.split(",")
	return gquestions

def game(gquestions):
	cnt  = 0
	for q,a in gquestions.items():
		print(q)
		correct = a[0]
		random.shuffle(a)
		for el in a:
			print(el)
		answer = input("Enter your answer: ")
		if answer == correct:
			print("Correct")
			cnt += 1
		else:
			print("Incorrect. The correct answer was", correct)

	print("You got %d/5" %cnt)
	return cnt

def get_questions_from_file(fname):
	with open(fname) as f:
		return f.readlines()

def sanitize_data(ml):
	return [el.strip() for el in ml]

def check_file_existence(fname):
	if not os.path.isfile(fname):
		print("Your files does not exists: %s. Please check" %fname)
		return False
	return True

def get_top_players_from_file(fname):
	with open(fname) as f:
		return f.readlines()

def create_file(fname):
	f = open(fname, "w")
	f.close()

def create_players_dict(data):
	# should be written "username: XP"
	md = {}
	for el in data:
		p,x = el.split(": ")
		md[p] = int(x)
	return md
	
def confirm_username(username, players):	
	if username in players:
		ans = input("Would you like to rewrite your XP? ")
		if ans.lower() == "y":
			pass
		else:
			username = input("Enter your username: ")
			while username in players:
				username = input("Enter your username: ")
	return username

def sort_players_by_xp(players):
	ml = list(players.items())
	ml.sort(key=lambda x: x[1], reverse=True)
	return ml

def write_player_xp(fname, ml):
	with open(fname, "w") as f:
		for pl, xp in ml:
			f.write(pl + ": " + str(xp) + "\n")

def main():
    question_file = "questions.txt"
    fl = check_file_existence(question_file)
    if not fl:
    	exit()
    adding_questions(question_file)
    username = input("Enter your username: ")
    top_file = "top_players.txt"
    fl = check_file_existence(top_file)
    if not fl:
        create_file(top_file)
    players_data = get_top_players_from_file(top_file)
    players = sanitize_data(players_data)
    players_dict = create_players_dict(players)
    username = confirm_username(username, players_dict)
    questions = get_questions_from_file(question_file)
    questions = sanitize_data(questions)
    random5 = get_random_5_questions(questions)
    game_questions = structure_questions(random5)
    xp = game(game_questions)
    players_dict[username] = xp
    players = sort_players_by_xp(players_dict)
    write_player_xp(top_file, players)

main()





