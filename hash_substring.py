def read_input():
    # read pattern and text from standard input
    pattern = input().rstrip()
    text = input().rstrip()
    return pattern, text

def print_occurrences(output):
    # print positions of occurrences
    print(' '.join(map(str, output)))

def get_occurrences(pattern, text):
    # initialize variables
    p = 10**9 + 7   # prime number for hashing
    x = 263         # base for hashing
    result = []
    p_hash = 0      # hash value for pattern
    t_hash = 0      # hash value for first substring of text
    x_power = 1     # x^m where m is length of pattern
    
    # calculate hash values for pattern and first substring of text
    for i in range(len(pattern)):
        p_hash = (p_hash * x + ord(pattern[i])) % p
        t_hash = (t_hash * x + ord(text[i])) % p
        if i < len(pattern) - 1:
            x_power = (x_power * x) % p
    
    # slide substring of length pattern over text
    for i in range(len(text) - len(pattern) + 1):
        if p_hash == t_hash:
            # check character by character to confirm match
            match = True
            for j in range(len(pattern)):
                if text[i+j] != pattern[j]:
                    match = False
                    break
            if match:
                result.append(i)
        # recalculate hash value for next substring
        if i < len(text) - len(pattern):
            t_hash = (x * (t_hash - ord(text[i]) * x_power) + ord(text[i+len(pattern)])) % p
            if t_hash < 0:
                t_hash += p
    
    return result

# main function
if __name__ == '__main__':
    pattern, text = read_input()
    occurrences = get_occurrences(pattern, text)
    print_occurrences(occurrences)
