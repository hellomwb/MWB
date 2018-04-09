from random import randint

num = randint(1, 100)
print 'Guess what I think?'
bingo=False

while bingo==False:
       answer = input()
       if answer<num:
            print '%s too small!'%answer
       if answer>num:
            print '%s too big!' %answer
       if answer==num:
            print 'BINGO! %s is the right answer!' %answer
            bingo=True