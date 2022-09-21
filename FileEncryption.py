def main():
    
    codes = {'A':'%', 'a':'9', 'B':'@', 'b':'#', 'C':'1', 'c':'2', 'D':'3', 'd':'4', \
             'E':'5', 'e':'6', 'F':'7', 'f':'8', 'G':'0', 'g':'}', 'H':'{', 'h':']', 'I':'[', 'i':'Y', \
             'J':'Z', 'j':'>', 'K':'<', 'k':'/', 'L':'j', 'l':'_', 'M':'"', 'm':'i', 'N':';', \
             'n':'A', 'O':'h', 'o':'-', 'Q':'$', 'q':'V', 'R':'^', 'r':'&', 'S':'^', \
             's':'(','T':')', 't':'~', 'U':'`', 'u':'g', 'V':'\\', 'v':'+', 'W':'=', 'w':'!', \
             'X':'f', 'x':'e', 'Y':'d', 'y':'c', 'Z':'b', 'z':'a'}
    
    encryption(codes)
    
    decryption(codes)

def encryption(codes):
    # Open file with normal message and read it
    myfile = open('info_security.txt', 'r')
    my_file_read = myfile.read()

    # Open file where decrypted message will be write
    # If not exists, it will create one
    encrypted_file = open('encrypted.txt', 'w')

    # Read every character in file
    for ch in my_file_read:
        # If current character is present in codes dictionary
        # Write it's value to decryptedMessage.txt
        # Else, write it as it is
        if ch in codes:
            encrypted_file.write(codes[ch])
        else:
            encrypted_file.write(ch)

    # Close file
    encrypted_file.close()


def decryption(codes):

    # Open decrypted file and read it
    encrypted_file = open('encrypted.txt', 'r')
    encrypted_file_read = encrypted_file.read()

    # Iterate over each character in decrypted file
    # Check if its not present in codes value field, then print it
    # If it's '.' or ' ', then also print it
    # Else, print key to the corresponding matched value
    for ch in encrypted_file_read:
        if not ch in codes.values() or ch == '.' or ch == ' ':
            print(ch, end='')
        else:
            for k, v in codes.items():
                if ch == v:
                    print(k, end='')  

main()      