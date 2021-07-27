import random

while True:
    flag = True
    while flag:
        num = input( 'Pick Any Number: ')

        if num.isdigit() :
            print("Let's play!!")
            num = int(num)
            flag = False
        else:
            print('Wrong Number! Try Again!!')

    secret = random.randint(1,num)

    guess = None
    count = 1

    while guess != secret:
        guess = input('Please type a numebr between 1 and ' + str(num) + ": ")
        if guess.isdigit():
            guess = int(guess)

        if guess == secret:
            print('Thats Right! Good Job!')
        else:
            print('Wrong! Play Again =)!')
            count += 1
            

    print('It took you', count, 'guess!')
                      
        
