# Exercise 2:
#
# Move the last line of this program to the top,
# so the function call appears before the definitions.
# Run the program and see what error message you get.

repeat_lyrics()

def print_lyrics():
  print("I'm a worker")
  
def repeat_lyrics():
  print_lyrics()
  print_lyrics()
