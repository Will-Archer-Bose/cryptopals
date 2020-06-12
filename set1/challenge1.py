import codecs

def hex_to_base64(hex_string):
    hex_bytes = codecs.decode(hex_string, "hex")
    # print(hex_bytes)
    base64_bytes = codecs.encode(hex_bytes, "base64")
    # print(base64_bytes)
    return base64_bytes.decode()[:-1]

if __name__ == "__main__":
    inp = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"
    expected = "SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t"
    out = hex_to_base64(inp)
    print(out == expected)