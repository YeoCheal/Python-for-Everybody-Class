# Exercise 2
#
# Rewrite your pay program using try and except
# so that your program handles non-numeric input gracefully
# by printing a message and exiting the program.
# The following shows two execitions of the program :


try :
  hrs = input('Enter Hours : ')
  rate = input('Enter Rate : ')

  hrs = float(hrs)
  rate = float(rate)

  if hrs > 40 :
    pay = ((hrs - 40) * rate * 1.5) + (40 * rate)
    print(pay)
  else :
    pay = hrs * rate
    print(pay)
    
except :
  print('Error, please enter numeric input')
  
  
