import string, codecs, math

def get_counts(str):
    count_dict = dict()
    for char in str:
        if char in count_dict.keys():
            count_dict[char] = count_dict[char] + 1
        else:
            count_dict[char] = 1
    return count_dict

def count_to_frequency(count_dict):
    total_count = sum([value for value in count_dict.values()])
    frequency_dict = dict([(key, count_dict[key]/total_count) for key in count_dict.keys()])
    return frequency_dict

def evaluate_output(output, fit_frequencies):
    output = output.lower()
    for char in output:
        # if any characters are not in normal ASCII space (32-126), throw it out
        if ord(char) < 32 or ord(char) > 126:
            return 1
    count_dict = get_counts(output)
    frequency_dict = count_to_frequency(count_dict)
    difference = 0
    for letter in fit_frequencies.keys():
        if letter in frequency_dict.keys():
            difference += math.pow(frequency_dict[letter] - fit_frequencies[letter], 2)
        else:
            difference += math.pow(fit_frequencies[letter], 2)
    return difference

def xor_cipher(code, fit_frequencies):
    ascii_code = codecs.decode(code, "hex").decode("ascii")
    results = dict()
    for letter in string.ascii_letters:
        result = "".join(
                        map(
                            lambda h: chr(ord(h) ^ ord(letter)),
                            ascii_code
                        )
                    )
        results[letter] = (evaluate_output(result, fit_frequencies), result)
    sorted_results = sorted(results.items(), key=lambda x: x[1][0])
    return sorted_results[0]
        

letter_count = dict([("e", 21912), ("t", 16587), ("a", 14810), ("o", 14003), ("i", 13318), ("n", 12666), 
                     ("s", 11450), ("r", 10977), ("h", 10795), ("d", 7874),  ("l", 7253),  ("u", 5246), 
                     ("c", 4943),  ("m", 4761),  ("f", 4200),  ("y", 3853),  ("w", 3819),  ("g", 3693), 
                     ("p", 3316),  ("b", 2715),  ("v", 2019),  ("k", 1257),  ("x", 315),   ("q", 205), ("j", 188),("z", 128)])
# source = pi.math.cornell.edu

english_frequencies = count_to_frequency(letter_count)

if __name__ == "__main__":
    code = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"
    best = xor_cipher(code, english_frequencies)
    print(f'{best[0]} --> {best[1][1]}')