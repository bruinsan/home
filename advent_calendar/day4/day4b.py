


def check_passphrase(phrase):
    listed_phrase = phrase.split()
    sorted_phrase = list()
    for word in listed_phrase:
        sorted_phrase.append(''.join(sorted(word)))
    
    for word in sorted_phrase:
        if sorted_phrase.count(word) > 1:
            return False
    return True


file_name = "input.txt"
with open(file_name, "r") as fl:
    count = 0
    for phrase in fl:
        if check_passphrase(phrase):
            count += 1

    print count
