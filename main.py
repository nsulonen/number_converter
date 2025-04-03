from converters import Decimal, Binary, Hexadecimal

def main() -> None:
    user_input = input('Enter a number: ')
    decimal: int = int(user_input)
    try:
        print(Decimal.to_bin(decimal))
    except Exception as e:
        print(e)
    


if __name__ == '__main__':
    main()