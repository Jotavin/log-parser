from parser_quake import parser_quake
import os

def main():
    games, means_death = parser_quake()
    while True:
        print('1. Players info')
        print('2. Means of death info')
        print('3. Show both')
        print('4. Exit')
        op = int(input('Input: '))

        os.system('cls')

        if op == 4:
            break
        elif op == 1:
            for game in games:
                 print(game.get_game_info())
        elif op == 2:
            for item in means_death:
                print(item.get_means_death())
        elif op == 3:
            for game in games:
                print(game.get_game_info())
            print('-'*30)
            for item in means_death:
                print(item.get_means_death())

        else:
            print('Choose an valid option')

if __name__ == '__main__':
    main()