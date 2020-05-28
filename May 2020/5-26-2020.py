"""
@author Zach Stoebner
@date 5-26-2020
@details Implement a function that converts a hex string to base64.

For example, the string:

deadbeef
should produce:

3q2+7w==
"""
import base64

# hex2base64
# Takes a hex string (aka containing only characters in the hex alphabet) and converts it to base 64
# Complexity: O(n)
def hex2base64(string: str):
    alpha64 = {0b000000:'A',0b010000:'Q',	0b100000:'g',0b110000:'w',
    0b000001:'B',0b010001:'R',0b100001:'h',	0b110001:'x',
    0b000010:'C',0b010010:'S',0b100010:'i',0b110010:'y',
    0b000011:'D',0b010011:'T',0b100011:'j',0b110011:'z',
    0b000100:'E',0b010100:'U',0b100100:'k',0b110100:'0',
    0b000101:'F',0b010101:'V',0b100101:'l',0b110101:'1',
    0b000110:'G',0b010110:'W',0b100110:'m',0b110110:'2',
    0b000111:'H',0b010111:'X',0b100111:'n',0b110111:'3',
    0b001000:'I',0b011000:'Y',0b101000:'o',0b111000:'4',
    0b001001:'J',0b011001:'Z',0b101001:'p',0b111001:'5',
    0b001010:'K',0b011010:'a',0b101010:'q',0b111010:'6',
    0b001011:'L',0b011011:'b',0b101011:'r',0b111011:'7',
    0b001100:'M',0b011100:'c',0b101100:'s',0b111100:'8',
    0b001101:'N',0b011101:'d',0b101101:'t',0b111101:'9',
    0b001110:'O',0b011110:'e',0b101110:'u',0b111110:'+',
    0b001111:'P',0b011111:'f',0b101111:'v',0b111111:'/'}

    alpha16 = {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'a':10,'A':10,
    'b':11,'B':11,'c':12,'C':12,'d':13,'D':13,'e':14,'E':14,'f':15,'F':15}

    num = 0
    n = len(string)
    for i,c in enumerate(string):
        num += alpha16[c]*(16**(n-i))

    mod = 0
    div = 0
    new_str = ""
    while num != 0:
        mod = num % 64
        div = num // 64

        new_str = alpha64[mod] + new_str

        num = div

    pad = len(new_str) % 4
    if pad != 0:
        new_str += (4-pad)*'='

    return new_str

### TESTS
print(hex2base64("deadbeef"))
#print(base64.b64encode("deadbeef"))

### ADMIN SOLUTION
def sextet_to_char(sextet):
    i = int(sextet, 2)
    if 0 <= i <= 25:
        return chr(i + 65)
    elif 26 <= i <= 51:
        return chr(i + 71)
    elif 52 <= i <= 61:
        return str(i - 52)
    elif i == 62:
        return '+'
    elif i == 63:
        return '/'
    else:
        raise Exception('Invalid sextet.')


def convert_hex_to_base64(s):
    b = bytearray.fromhex(s)

    # Convert to bit string.
    bit_string = ''
    for c in b:
        bit_string += bin(c)[2:].zfill(8)

    # Calculate padding and pad rest of string with 0s.
    padding = 6 - len(bit_string) % 6
    bit_string += '0' * padding

    # Break down bit string into sextets and convert to base64 chars.
    result = ''
    for i in range(0, len(bit_string), 6):
        sextet = bit_string[i:i + 6]
        result += sextet_to_char(sextet)

    # Add equal sign padding
    result += '=' * (padding / 2)

    return result
