class Decimal:
    @staticmethod
    def to_bin(decimal: int) -> str:
        if decimal < 0:
            raise ValueError('Input must be non-negative integer.')

        if decimal <= 1:
            return str(decimal)
        else:
            return Decimal.to_bin(decimal // 2) + str(decimal % 2)

    @staticmethod
    def to_hex(decimal: int) -> str:
        hex_symbols = '0123456789ABCDEF'

        if decimal < 0:
            raise ValueError('Input must be non-negative integer.')
        elif decimal < 1:
            return hex_symbols[decimal]

        return f'{Decimal.to_hex(decimal // 16)}{hex_symbols[decimal % 16]}'

class Binary:
    @staticmethod
    def to_dec(binary: str) -> int:
        if not binary:
            return 0
        else:
            return int(binary[-1]) + 2 * Binary.to_dec(binary[:-1])

    @staticmethod
    def to_hex(binary: str) -> str:
        return Decimal.to_hex(Binary.to_dec(binary))

class Hexadecimal:
    @staticmethod
    def to_dec(hexadecimal: str, n: int = 0) -> int:
        hex_symbols = '0123456789ABCDEF'

        if not hexadecimal:
            return 0
        return hex_symbols.index(hexadecimal[-1]) * 16**n + Hexadecimal.to_dec(hexadecimal[:-1], n+1)

    @staticmethod
    def to_bin(hexadecimal: str) -> str:
        return Decimal.to_bin(Hexadecimal.to_dec(hexadecimal))