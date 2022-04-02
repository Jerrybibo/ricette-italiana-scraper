from settings import *

DEBUG = False


def print_motd(): print(MOTD)
def print_help(): print(HELP_MSG)


def program_exit():
    print('Bye!')
    exit(0)


def debug():
    global DEBUG
    DEBUG = not DEBUG
    print("Debug mode: {}".format(DEBUG))


def main():
    methods = {
        'motd': print_motd,
        'help': print_help,
        'exit': program_exit,
        'debug': debug
    }
    print_motd()
    while True:
        user_input = [word for word in input("> ").strip().lower().split()]
        if not user_input:
            print("Please enter a command.")
        elif user_input[0] in methods:
            methods[user_input[0]]()
        else:
            print(f"Unknown command '{user_input[0]}'. Type 'help' for a list of commands.")


if __name__ == '__main__':
    main()
