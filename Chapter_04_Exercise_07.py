# Exercise 7:
#
# Rewrite the grade program from the previous chapter using
# a function called computegrade that takes a score as its
# parameter and returns a grade as a string.

def computegrade():
    try:
        score = input('Enter socre :')
        score = float(score)
        if score > 1.0:
            print('Bad score')
        elif score >= 0.9 and score <= 1.0:
            print('A')
        elif score >= 0.8 and score < 0.9:
            print('B')
        elif score >= 0.7 and score < 0.8:
            print('C')
        elif score >= 0.6 and score < 0.7:
            print('D')
        elif score < 0.6 and score >= 0.0:
            print('F')
        else:
            print('Bad score')
            quit()

    except:
        print('Bad score')
        quit()


computegrade()
