#Program to Guess The Number in My Head
#This is without the random module
print 'Are you ready to play? Try to guess the number in my head'
lucky = 13
guess = int(raw_input('Enter a number between 1 and 20: '))


while lucky != guess:
    print
    if guess < lucky:
        print 'Too low! Go a little higher!'
        guess = int(raw_input('Enter a number between 1 and 20: '))

    elif guess >= 21:
        print 'Enter a valid number between 1 and 20! Anything above is not valid'
        guess = int(raw_input('Enter a number between 1 and 20: '))

    elif guess > lucky:
        print 'Too high! Go a little lower!'
        guess = int(raw_input('Enter a number between 1 and 20: '))

    if guess == lucky:
        print 'You guessed it!'
        break
    print

