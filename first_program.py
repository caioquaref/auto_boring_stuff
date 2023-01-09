import datetime

print('\nHello there!\n\nThis program is inspired by Automate the Boring Stuff with Python. Would you like do procede?')

def answer_one():
    userInput = input('\nAnswer with Y key for Yes or N key for No: ')  # Local variable, it's in answer_one()'s scope.

    if userInput == 'Y' or userInput == 'y':
        pass
    elif userInput == 'N' or userInput == 'n':
        print('\nSee ya later, alligator!')
        quit()
    else:
        print('\nInvalid key!')
        answer_one()  # The function calls itself.

answer_one()

print('\nWhat is your full name and birthdate?')
userName = input('Your full name: ')  # Global variable.

def age_check():
    global userBirth  # "Calls" global variable: userName.
    userBirth = input('Birthdate (dd/mm/yyyy): ')  # userBirth: local variable.
    date_format = "%d/%m/%Y"  # requested date format.

    try:  # Try block: to prevent crashing if user inputs the wrong date format.
        dt_object = datetime.datetime.strptime(userBirth, date_format)  # From string to datetime datatype.
        
    except ValueError:  # If user inputs the wrong date format:
        print('Unsupported date format!')
        age_check()  # The function calls itself.
    
age_check()

print('\nNice to meet you, ' + userName + '!\nWould you like to see some stats about yourself?')

answer_one()

print('\n1. Your name is ' + str(len(userName)) + ' characters long.')

surnameInitialsIndex = [x+1 for x, z in enumerate(userName) if z == ' ']  #List comprehension
initials_index = [0] + surnameInitialsIndex

initials = []
for i in initials_index:
    letter = userName[i]
    initials.append(letter)
print('2. Your initials are: ' + ''.join(map(str,initials)))

date_format = "%d/%m/%Y"
dt_object = datetime.datetime.strptime(userBirth, date_format)
age = datetime.datetime.now() - dt_object

print('3. You are ' + str(age.days) + ' days old, hope you already know how old you are!')
print('\n\nThanks for running this program, many more are to come! :)\n------------------------')
