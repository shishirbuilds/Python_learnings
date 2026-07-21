#to install this module : python -m pip install pyjokes
#this module is used to print random jokes

import pyjokes
print("Printing a Joke: ")
joke = pyjokes.get_joke()
print(joke)