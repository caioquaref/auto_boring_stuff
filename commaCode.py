spam = ['apples', 'bananas', 'tofu', 'cats', 'beavers']
emp = ['GOD DMAN, THE PUSHER!']

def commaCode(listInput):
    print('\n\n')
    if len(listInput) == 0:
        quit('Your list is empty.')
    elif len(listInput) == 1:
        print('{}'.format(str(listInput)))
    else:
        for x in range(len(listInput)):
            if (x - len(listInput)) != -1:
                print(listInput[x], end=', ')
            else:
                print(' and ', listInput[x])

commaCode(spam)