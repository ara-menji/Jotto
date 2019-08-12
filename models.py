from google.appengine.ext import ndb

import webapp2
import jinja2

import os
import random

class WordDifficulty(ndb.Model):

  def difficulty(self):

    if self.difficulty == 'jotto_beginner_word':
        word = "key"
    elif self.difficulty == 'jotto_medium_word':
        word = "try"
    elif self.difficulty == 'jotto_hard_word':
        word = "way"
    return word

class JottoWord(ndb.Model):

    jotto_word_list=[str("fox"),str("hot"),str("try"),str("cry"),str("way")]
    jotto_word=jotto_word_list[random.randint(0,(len(jotto_word_list)-1))]
    jotto_word_set=set(jotto_word)

class GuessWord(ndb.Model):

    guess = ndb.StringProperty(required=True)
