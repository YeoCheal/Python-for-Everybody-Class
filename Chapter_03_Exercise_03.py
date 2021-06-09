# Exercise 3
#
# Write a program to prompt for a score between 0.0 and 1.0.
# If the score is out of range, print an error message.
# If the score is between 0.0 and 1.0, print a grade using
# the following table :


try :
  pmt = input('Enter score : ')
  pmt = float(pmt)

except :
  print('Bad score')
  quit()
  
if pmt > 1.0 :
  print('Bad score')
elif pmt >= 0.9 and pmt <= 1.0 :
  print('A')
elif pmt >= 0.8 and pmt < 0.9 :
  print('B')
elif pmt >= 0.7 and pmt < 0.8 :
  print('C')
elif pmt >= 0.6 and pmt < 0.7 :
  print('D')
elif pmt < 0.6 and pmt >= 0.0 :
  print('F')
else :
  print('Bad score')
  
  
