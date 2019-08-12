import webapp2
import jinja2
import os
import random
import re
import time
import math
import sys
import os
import subprocess

from models import GuessWord
from models import JottoWord

the_jinja_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

jotto_welcome_statement = str("Welcome to the Jotto WebApp.")
# print(jotto_welcome_statement)

jotto_word_length_statement = str("The random words in this instance of the game have 3 letters.")
print(jotto_word_length_statement)

jotto_easy_word = "key"
jotto_easy_word_set=set(jotto_easy_word)

jotto_medium_word = "try"
jotto_medium_word_set=set(jotto_medium_word)

jotto_hard_word = "way"
jotto_hard_word_set=set(jotto_hard_word)

jotto_random_word_list=[str("fox"),str("hot"),str("try"),str("cry"),str("way")]
jotto_random_word=jotto_random_word_list[random.randint(0,(len(jotto_random_word_list)-1))]
jotto_random_word_set=set(jotto_random_word)

jotto_difficulty_list1 = ["Hard", "Medium", "Easy", "Random"]
jotto_difficulty_list2 = [float(1), float(2), float(3), float(4)]
jotto_hard_difficulty_statement = str("Input 1 for " + str(jotto_difficulty_list1[0]))
jotto_medium_difficulty_statement = str("Input 2 for " + str(jotto_difficulty_list1[1]))
jotto_easy_difficulty_statement = str("Input 3 for " + str(jotto_difficulty_list1[2]))
jotto_random_difficulty_statement = str("Input 4 for " + str(jotto_difficulty_list1[3]))

# print(jotto_hard_difficulty_statement)
# print(jotto_medium_difficulty_statement)
# print(jotto_easy_difficulty_statement)
# print(jotto_random_difficulty_statement)

# difficulty_number = float(raw_input("Enter your choice from the options above to select your desired difficulty level: "))

# if difficulty_number in jotto_difficulty_list2:
#
#     guess = str(raw_input("Guess a word with 3 letters: ")).lower()
#     guess_set=set(guess)
#
#     if difficulty_number == 4:
#         print("You have selected the random difficulty word.")
#         if len(guess_set) == 3:
#             if jotto_random_word==guess:
#                 print("Congratulations, you have won. The word was " + str(jotto_random_word))
#                 print("Your guess has " + str(len(guess_set)) + " common letters.")
#             else:
#                 if len(guess_set&jotto_random_word_set) > 1:
#                     print("Your guess has " + str(len(guess_set&jotto_hard_word_set)) + " common letters.")
#                 else:
#                     print("Your guess has " + str(len(guess_set&jotto_hard_word_set)) + " common letter.")
#                 print("Sorry, you have not won. If you try again, you may not be guessing the same random word.")
#         else:
#             print str("Sorry, you need to enter a word consisting of 3 different letters.")
#
#     elif difficulty_number == 1:
#         print("You have selected the hard difficulty word.")
#         if len(guess_set) == 3:
#             if jotto_random_word==guess:
#                 print("Congratulations, you have won. The word was " + str(jotto_random_word))
#                 print("Your guess has " + str(len(guess_set)) + " common letters.")
#             else:
#                 if len(guess_set&jotto_random_word_set) > 1:
#                     print("Your guess has " + str(len(guess_set&jotto_hard_word_set)) + " common letters.")
#                 else:
#                     print("Your guess has " + str(len(guess_set&jotto_hard_word_set)) + " common letter.")
#                 print("Sorry, you have not won. If you try again, you may not be guessing the same random word.")
#         else:
#             print str("Sorry, you need to enter a word consisting of 3 different letters.")
#
#     elif difficulty_number == 2:
#         print("You have selected the medium difficulty word.")
#         if len(guess_set) == 3:
#             print("Your guess has " + str(len(guess_set&jotto_medium_word_set)) + " common letters.")
#             if jotto_medium_word==guess:
#                 print("Congratulations, you have won. The word was " + str(jotto_medium_word))
#             else:
#                 print("Sorry, you have not won. You may try again by selecting the same difficulty.")
#         else:
#             print str("Sorry, you need to enter a word consisting of 3 different letters.")
#
#     elif difficulty_number == 3:
#         print("You have selected the easy difficulty word.")
#         if len(guess_set) == 3:
#             print("Your guess has " + str(len(guess_set&jotto_easy_word_set)) + " common letters.")
#             if jotto_easy_word==guess:
#                 print("Congratulations, you have won. The word was " + str(jotto_easy_word))
#             else:
#                 print("Sorry, you have not won. You may try again by selecting the same difficulty.")
#         else:
#             print str("Sorry, you need to enter a word consisting of 3 different letters.")
#
# else:
#     print(str("The number you entered does not have a corresponding difficulty level."))

class MainPageHandler(webapp2.RequestHandler):
    def get(self):
        MainPageHandler_template = the_jinja_env.get_template("templates/MainPageHandler.html")
        self.response.write(MainPageHandler_template.render())
    def post(self):
        MainPageHandler_template = the_jinja_env.get_template("templates/MainPageHandler.html")
        self.response.write(MainPageHandler_template.render())

class GamePageHandler(webapp2.RequestHandler):
    def get(self):
        GamePageHandler_template = the_jinja_env.get_template('templates/GamePageHandler.html')
        self.response.write(GamePageHandler_template.render())
    def post(self):
        GamePageHandler_template = the_jinja_env.get_template('templates/GamePageHandler.html')
        self.response.write(GamePageHandler_template.render())

class ResultsPageHandler(webapp2.RequestHandler):
    def get(self):
        ResultsPageHandler_template = the_jinja_env.get_template('templates/ResultsPageHandler.html')
        self.response.write(ResultsPageHandler_template.render())
    def post(self):
        ResultsPageHandler_template = the_jinja_env.get_template('templates/ResultsPageHandler.html')
        self.response.write(ResultsPageHandler_template.render())

class UserListPageHandler(webapp2.RequestHandler):
    def get(self):
        UserListPageHandler_template = the_jinja_env.get_template('templates/UserListPageHandler.html')
        self.response.write(UserListPageHandler_template.render())
    def post(self):
        UserListPageHandler_template = the_jinja_env.get_template('templates/UserListPageHandler.html')
        self.response.write(UserListPageHandler_template.render())

app = webapp2.WSGIApplication([
    ('/', MainPageHandler),
    ('/main', MainPageHandler),
    ('/game', GamePageHandler),
    ('/results', ResultsPageHandler),
    ('/users', UserListPageHandler),
], debug=True)
