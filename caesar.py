import string

def alphabet_position(letter):
    """Get's the position of the letter in the alphabet starting a = 0"""
    alphabetLower = string.ascii_lowercase
    alphabetUpper = string.ascii_uppercase

    for idx, alpha in enumerate(alphabetLower):
        if alpha == letter:
            return(idx)
    
    for id, alp in enumerate(alphabetUpper):
        if alp == letter:
            return(id)

def rotate_character(char, rot):
    """Changes the character number of rotations ahead in the alphabet"""
    if rot == 0:
        return(char)
    try:
        pos = alphabet_position(char)
        number = pos + rot
    except TypeError:
        return(char)   
       
    x = 0
    aroundAlph = number // 25
    x = number % 25
    if x == 0:
        x = pos
    else:
        if aroundAlph >= 0:
            x = x - aroundAlph
    #print(char, ':', x)

    alphabetLower = string.ascii_lowercase
    alphabetUpper = string.ascii_uppercase
    
    if char in alphabetLower:
        newLetter = alphabetLower[x]
        return(newLetter)
    if char in alphabetUpper:
        newLetter = alphabetUpper[x]
        return(newLetter)

def rotate_string(text, rot):
    newText = ''

    for letter in text:
        newLetter = rotate_character(letter, rot)
        newText  = newText + newLetter
    return(newText)
