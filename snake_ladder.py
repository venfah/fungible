import sys
from random import randint 
from signal import signal, SIGINT

auto_mode = True
# auto_mode = False
users = {}

def handle (signal, frame):
    print ("\nCTRL+C detected. Quiting\n")
    print ("Current positions:\n")
    for each in users.keys():
        print ("{} at: {}".format(each, users[each]['current']))
    sys.exit(1)

signal(SIGINT, handle)


def get_user_name(no):
    try:
        return (raw_input("User{} Name: ".format(no + 1)).rstrip())
    except NameError:
        return (input("User{} Name: ".format(no + 1)).rstrip())

def throw_dice(user):
    if (auto_mode):
        return (randint(1, 12))
    else:
        if user:
            while True:
                no = 0
                try:
                    no = raw_input("Throw the dice manually, {} and enter:".format(user)).rstrip()
                except NameError:
                    no = input("Throw the dice manually, {} and enter:".format(user)).rstrip()
                if no.isdigit() == True and int(no) > 0 and int(no) <= 12:
                    return int(no)
                    break
                else:
                    print ("{} not a valid no: enter again".format(no))

def check_win (user):
    if users[each]['current'] >= 100:
        print ("User {} won the match. Congratulations. Quitting...!".format(user))
        return True
    return False

No_Users = 2
#for each in range(0, No_Users):
#    users[get_user_name(each)] = {'current':0}
users = {'Nazir':{'current' :0}, 'Venfah':{'current' :0}}

snake  = {20:5, 40:12, 60:4, 80: 35, 98:52, 75:70, 93:9}
ladder = {8:31, 22:65, 38:94, 62:72, 45:51}

game_over = False 

while True:
    for each in users.keys():
        print ("User {} throws dice: ".format(each))
        users[each]['current'] += throw_dice(each)
        game_over = check_win(each)
        print ("User {} current position: {}".format(each, users[each]['current']))
        if (game_over): break


        if (users[each]['current'] in snake):
            print ("User {} found snake at {}. Go back to {}".format(each, users[each]['current'], snake[users[each]['current']]))
            users[each]['current'] = snake[users[each]['current']]
            print ("User {} current position: {}".format(each, users[each]['current']))

        if (users[each]['current'] in ladder):
            print ("User {} found ladder at {}. Go forward to {}".format(each, users[each]['current'], ladder[users[each]['current']]))
            users[each]['current'] = ladder[users[each]['current']]
            print ("User {} current position: {}".format(each, users[each]['current']))

            print ("User {} gets another chance throw dice: ".format(each))
            users[each]['current'] += throw_dice(each)
            print ("User {} current position: {}".format(each, users[each]['current']))
            game_over = check_win(each)
            if (game_over): break

    if (game_over): break


print ("{}".format(users))
