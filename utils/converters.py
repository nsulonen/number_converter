def bin_to_dec() -> None:
    raise NotImplementedError('bin_to_dec not implemented')

def dec_to_bin(n: int) -> None:
    if n < 0:
        raise ValueError('Input must be non-negative integer.')
    
    if n <= 1:
        return str(n)
    else:
        return dec_to_bin(n // 2) + str(n % 2)

def hex_to_dec() -> None:
    raise NotImplementedError('hex_to_dec not implemented')

def dec_to_hex() -> None:
    raise NotImplementedError('dec_to_hex not implemented')

def bin_to_hex() -> None:
    raise NotImplementedError('bin_to_hex not implemented')

def hex_to_bin() -> None:
    raise NotImplementedError('hex_to_bin not implemented')