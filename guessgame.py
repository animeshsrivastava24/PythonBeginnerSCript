import random
highest = 10
answer = random.randint(1,highest)
print(answer)
print('please guess a number from 1 and {}:'.format(highest))
guess = int(input())
if guess > answer:
    print('please guess lower')
    guess = int(input())
    if guess == answer:
        print('you won on 2nd attempt')
    else:
        print('sorry, incorrect guess')
elif guess < answer:
    print('please guess higher')
    guess = int(input())
    if guess == answer:
        print('you won on 3rd attempt')
    else:
        print('sorry,incorrect guess')
else:
    print('wow you nailed it on the first time')
