T = int(input())
encode = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
          'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f',
          'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
          'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '+', '/']

for test_case in range(1, T + 1):
    encoded_str = input()
    total_bin_str = ''
    result = ''

    for i in range(len(encoded_str)):
        encode_num = encode.index(encoded_str[i])
        bin_str = bin(encode_num)[2:]

        if len(bin_str) < 6:
            bin_str = bin_str.zfill(6)

        total_bin_str += bin_str

    for j in range(0, len(total_bin_str), 8):
        decimal_num = int('0b' + total_bin_str[j:j+8], 2)
        result += chr(decimal_num)

    print("#{} {}".format(test_case, result))
