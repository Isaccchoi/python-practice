import game
import shop
from friends.chat import send_message

def turn_on():
    print('=Turn on game =')

    while True:
        choice = input('What would you like to do?\n 1: Go Go Shop, 2:Play Game, 3:Message 0: Exit\n Input: ')
        if choice == '0':
            break
        elif choice == '1':
            shop.buy_item()
        elif choice == '2':
            game.play_game()
        elif choice == '3':
            send_message()
        else:
            print('Choice not exist')
        print('--------------------------')

    print('==Turn off game==')


if __name__ == '__main__':
    turn_on()
