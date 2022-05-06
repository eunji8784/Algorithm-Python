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
        # encoding된 문자에 해당하는 값 읽어오기
        encode_num = encode.index(encoded_str[i]) 
          
        # bin 함수를 이용해 이진수로 변환한 뒤 '0b' 문자 제거
        bin_str = bin(encode_num)[2:] 

        # 이진수 자릿수가 6 미만인 경우에는 zfill 메서드를 이용해 부족한 자릿수만큼 0으로 채움
        if len(bin_str) < 6:
            bin_str = bin_str.zfill(6)

        # 전체 문자열의 이진수 변환 값 저장
        total_bin_str += bin_str

    # 이진수를 8비트씩 끊어서 십진수로 변환한 뒤 ascii 문자로 바꿈
    for j in range(0, len(total_bin_str), 8):
        decimal_num = int('0b' + total_bin_str[j:j+8], 2)
        result += chr(decimal_num)

    print("#{} {}".format(test_case, result))
