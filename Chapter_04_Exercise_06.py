# Exercise 6:
#
# Rewrite your pay computation with time-and-a-half for overtime
# and create a function called computepay which takes two
# parameters(hours and rate).


try:
    hrs = input('Enter hours :')
    hrs = float(hrs)

    rate = input('Enter a rate :')
    rate = float(rate)


    if hrs > 40:
        pay = (40 * rate) + (hrs - 40) * (rate * 1.5)
        print(pay)

    else :
        pay = hrs * rate
        print(pay)


except:
    print('Error, Please input the number.')

