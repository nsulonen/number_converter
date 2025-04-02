

def bin_to_dec(binary: str) -> int:
    if not binary:
        return 0
    else:
        return int(binary[-1]) + 2 * bin_to_dec(binary[:-1])

def dec_to_bin(decimal: int) -> str:
    if decimal < 0:
        raise ValueError('Input must be non-negative integer.')

    if decimal <= 1:
        return str(decimal)
    else:
        return dec_to_bin(decimal // 2) + str(decimal % 2)

def hex_to_dec(hexadecimal: str, n: int = 0) -> int:
    hex_symbols = '0123456789ABCDEF'

    if not hexadecimal:
        return 0
    return hex_symbols.index(hexadecimal[-1]) * 16**n + hex_to_dec(hexadecimal[:-1], n+1)


def dec_to_hex(decimal: int) -> str:
    hex_symbols = '0123456789ABCDEF'

    if decimal < 0:
        raise ValueError('Input must be non-negative integer.')
    elif decimal < 1:
        return ''

    return f'{dec_to_hex(decimal // 16)}{hex_symbols[decimal % 16]}'

def bin_to_hex(binary: str) -> str:
    return dec_to_hex(bin_to_dec(binary))

def hex_to_bin(hexadecimal: str) -> str:
    return dec_to_bin(hex_to_dec(hexadecimal))



def main() -> None:
    user_input = input('Enter a number: ')
    decimal: int = int(user_input)
    try:
        print(dec_to_bin(decimal))
        print(bin_to_dec(dec_to_bin(decimal)))
        print(dec_to_hex(decimal))
        print(hex_to_dec(dec_to_hex(decimal)))
        print(bin_to_hex(dec_to_bin(decimal)))
        print(hex_to_bin(dec_to_hex(decimal)))
    except Exception as e:
        print(e)
    


if __name__ == '__main__':
    main()