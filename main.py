print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

names = (name1 + " " + name2)

names = names.lower()
t = names.count("t")
r = names.count("r")
u = names.count("u")
e = names.count("e")

l = names.count("l")
o = names.count("o")
v = names.count("v")

true_count = str(t + r + u + e)

love_count = str(l + o + v+ e)

love_score = true_count + love_count

love_score_as_int = int(love_score)

if love_score_as_int < 10 or love_score_as_int > 90:
  print(f"Your score is {love_score_as_int}, you go together like coke and mentos.")
elif love_score_as_int >= 40 and love_score_as_int <= 50:
  print(f"Your score is {love_score_as_int}, you are alright together.")
else:
  print(f"Your score is {love_score_as_int}.")
