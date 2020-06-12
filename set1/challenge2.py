def fixed_xor(hex1, hex2):
    return hex(int(hex1, 16) ^ int(hex2, 16))[2:]

if __name__ == "__main__":
    hex1 = "1c0111001f010100061a024b53535009181c"
    hex2 = "686974207468652062756c6c277320657965"
    expected = "746865206b696420646f6e277420706c6179"
    out = fixed_xor(hex1, hex2)
    print(out == expected)
