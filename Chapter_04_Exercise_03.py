# Exercise 3:
#
# Move the function call back to the bottom and
# move the definition of print_lyrics after the
# definition of repeat_lyrics. What happens when
# you run this program?


def print_lyrics():
  print("I'm a worker")

def repeat_lyrics():
  print_lyrics()
  print_lyrics()
  

repeat_lyrics()


# I'm a worker
# I'm a worker
