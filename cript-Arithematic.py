from itertools import permutations

def encode_string(string, char_to_num):
    return int("".join(str(char_to_num[char]) for char in string))

def is_mapping_possible(arr, S):
    unique_chars = set("".join(arr + [S]))
    if len(unique_chars) > 10:
        return False
    
    for perm in permutations(range(10), len(unique_chars)):
        char_to_num = {char: num for char, num in zip(unique_chars, perm)}
        
        encoded_arr = [encode_string(string, char_to_num) for string in arr]
        encoded_S = encode_string(S, char_to_num)
        
        if sum(encoded_arr) == encoded_S:
            return True, char_to_num
    
    return False, None

arr = ["SEND", "MORE"]
S = "MONEY"

possible, char_to_num = is_mapping_possible(arr, S)
if possible:
    print("Yes")
    print("Numeric values of each letter:")
    for char, num in sorted(char_to_num.items()):
        print(f"{char}: {num}")
else:
    print("No")
