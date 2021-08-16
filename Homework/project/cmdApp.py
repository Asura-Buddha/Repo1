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
    return int(int(bin), 2)


def bin_to_char(bin_word: str):
    result = ''  # example: 11010010 = b
    '''
        returns char if binary code is known. 
    '''
    return result


def character_to_ascii(ch: str):
    result = 0  # example: s = 115
    '''
        return ascii code of character
    '''
    return ord(ch)


def text_to_binary(text: str):
    result = ''  # hello-> '01101000 01100101 01101100 01101100 01101111'
    '''
        returns binary string (chars are space separated) representing text
    '''
    for i in text:
        result += (number_to_binary(character_to_ascii(i)))
    return result


def encrypt(text: str, img, secret):
    new_img = img.convert('RGB')

    text_byte = text_to_binary(text)  # 01101000 01100101 01101100 01101100 01101111
    pixels = img.load()
    cnt = 0
    for x in range(img.size[0]):
        for y in range(img.size[1]):
            r_new = r = pixels[x, y][0]
            g_new = g = pixels[x, y][1]
            b_new = b = pixels[x, y][2]
            bin_r = number_to_binary(r)  # 1) convert r to binary
            bin_g = number_to_binary(g)  # 2) convert g to binary
            bin_b = number_to_binary(b)  # 3) convert b to binary
            # 4) for next three chars of text_byte
            bin_r[len(bin_r) - 1] = text_byte[0 + cnt]
            bin_g[len(bin_g) - 1] = text_byte[1 + cnt]
            bin_b[len(bin_b) - 1] = text_byte[2 + cnt]
            cnt += 3
            r_new = binary_to_decimal(bin_r)
            g_new = binary_to_decimal(bin_g)
            b_new = binary_to_decimal(bin_b)
        # change r_new's last chars
        # convert back to decimals
        # store the result in r_new

        pixels[i, j] = (r_new, b_new, g_new)


    # add secret message at the end!!!
    '''
        returns image with text encrypted
    '''
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
            if cnt == 8:
                text += " "
                cnt = 0
            text += r[len(r)-1]
            cnt += 1
            if cnt == 8:
                text += " "
                cnt = 0
            text += g[len(g) - 1]
            cnt += 1
            if cnt == 8:
                text += " "
                cnt = 0
            text += b[len(b) - 1]
            cnt += 1
            # 4) get LSBs
            # 5) store LSBs in text
            # 6) put space after every 8 characters

    result = ''

    for bin_word in text.split(' '):
        result += bin_to_char(bin_word)
    return result


def main():
    img = 'a.png'
    text = 'hello!'
    secret = '123'
    img_encrypted = encrypt(text, img, secret)
    img_encrypted.save('a_encryoted.jpg')
    img_encrypted.show()


if __name__ == '__main__':
    main()
