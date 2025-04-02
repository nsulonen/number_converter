from utils.converters import *

def main() -> None:
    user_input = int(input('Enter a number: '))
    try:
        print(dec_to_bin(user_input))
    except Exception as e:
        print(e)
    


if __name__ == '__main__':
    main()