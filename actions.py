# -*- coding: utf-8 -*-

def table(phenny, input):
   phenny.say('(╯°□°）╯︵ ┻━┻')
table.commands = ['table', 'rage']

def joyful(phenny, input):
   joyful_emotes = [ '🙌', '😀', '😁', '😂', '😃', '😄', '😅' ]
   from random import choice
   phenny.say(choice(joyful_emotes))
joyful.commands = [ 'huzzuh', 'awesome', 'happy', 'smile' ]
