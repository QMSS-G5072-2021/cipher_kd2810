def cipher(text, shift, encrypt=True):
    """Secure message through encryption.

    Message is encrypted by shifting each letter by the
    specified amount and direction.

    Parameters
    ----------
    text : str
        message to be encrypted.

    shift : int
        number of shifts added to each letter

    encrypt : bool
        direction of shift. (default = True)

    Returns
    -------
    str
        message encrypted by cipher technique

    Examples
    --------
    >>> cipher("quiet! It's a secret", 2, True)
    "swkgv! Kv'u c ugetgv"
    """
    alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    new_text = ''
    for c in text:
        index = alphabet.find(c)
        if index == -1:
            new_text += c
        else:
            new_index = index + shift if encrypt == True else index - shift
            new_index %= len(alphabet)
            new_text += alphabet[new_index:new_index+1]
    return new_text