from PIL import Image
# <----------  Math Begin -------------> 

def number_to_binary(num: int):
    result = ''  # example: 10 = '10100000'
    '''
        returns 8bit representation of int number
    '''
    return format(num, '08b')

def binary_to_decimal(bin: str):
    result = 0
    '''
        returns decimal value from binary STRING!!!
    '''
    return int(bin, 2)

def character_to_ascii(ch: str):
    # example: s = 115
    '''
        return ascii code of character
    '''
    return ord(ch)

def bin_to_char(bin_word: str):
    # 11010010 -> decimal repr
    # decimal -> char with that ASCII code
    '''
        returns char if binary code is known. 
    '''

    ascii_ch = binary_to_decimal(bin_word) 
    return chr(ascii_ch)

def text_to_binary(text: str):
    result = ''  # hello-> '01101000 01100101 01101100 01101100 01101111'
    '''
        returns binary string (chars are space separated) representing text
    '''
    for i in text:
        result += (number_to_binary(character_to_ascii(i))) 
        
    return result[:-1]



# <----------- Math End --------------->

# <----------  Image Processing Begin -------------> 
def encrypt(text: str, img, secret):
    text += secret
    new_img = img.convert('RGB')
    text_byte = text_to_binary(text)  # converts text tp binary string 01101000 01100101 01101100 01101100 01101111
    pixels = img.load() # 2d array or (0,255,121)
    cnt = 0
    message_len = len(text_byte)

    test = ''

    for x in range(img.size[0]):
        for y in range(img.size[1]):
            
            r_ascii = pixels[x, y][0] # 125
            g_ascii = pixels[x, y][1] # 083
            b_ascii = pixels[x, y][2] # 219

            r = number_to_binary(r_ascii)  # 1) convert r to binary # 10001101
            g = number_to_binary(g_ascii)  # 2) convert g to binary # 10001101
            b = number_to_binary(b_ascii)  # 3) convert b to binary # 10001101
            
            # 4) for next three chars of text_byte
            if (text_byte[cnt] == ' '):
                cnt += 1

            if (cnt < message_len):
                red_new = int(r[:-1] + text_byte[cnt], 2)
                cnt += 1
            else:
                red_new = r_ascii
            
            if (cnt < message_len):
                green_new = int(g[:-1] + text_byte[cnt], 2)
                cnt += 1
            else:
                green_new = g_ascii

            if (cnt < message_len):
                blue_new = int(b[:-1] + text_byte[cnt], 2)
                cnt += 1
            else:
                blue_new = b_ascii

            
            pixels[x,y] = (red_new, green_new, blue_new)
            test += number_to_binary(red_new)[-1]+number_to_binary(green_new)[-1]+number_to_binary(blue_new)[-1]
            if (cnt >= message_len):
                return new_img
    return new_img

def decrypt(img, secret):
    text = ''
    pixels = img.load()
    cnt = 0

    for x in range(img.size[0]):
        for y in range(img.size[1]):
            r = pixels[x, y][0]
            g = pixels[x, y][1]
            b = pixels[x, y][2]

            r = number_to_binary(r)  # 1) convert r to binary
            g = number_to_binary(g)  # 2) convert g to binary
            b = number_to_binary(b)  # 3) convert b to binary
            text += r[-1] + g[-1] + b[-1]

    text_split = [bin_to_char(text[i:i+8]) for i in range(0,len(text),8)]
    result = ''

    for ch in text_split:
        s = len(secret)*(-1)
        result += ch
        if result[s:] == secret:
            break


    return result

# <----------  Image Processing End -------------> 
def main():

    test = input('enc or dec: ')

    if (test == 'enc'):

    # < ----------- Encrypt example Begin ------------->

        path = input('File name: ')
        text_to_hide = input('Secret message: ')
        secret_key = input('Key: ')
        img = Image.open(path)
        img_encrypted = encrypt(text_to_hide, img, secret_key)
        img_encrypted.save('encrypted-'+path)
        img_encrypted.show()

    # < ----------- Encrypt example End ------------->

    else:



    # < ----------- Decrypt example Begin ------------->


        path = input('File name: ')
        secret_key = input('Key: ')
        img = Image.open(path)
        print(decrypt(img, secret_key))

    # < ----------- Decrypt example Begin ------------->


if __name__ == '__main__':
    main()