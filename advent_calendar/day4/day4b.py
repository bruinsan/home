


def check_passphrase(phrase):
    listed_phrase = phrase.split()
    for word in listed_phrase:
                     



file_name = "input.txt"
with open(file_name, "r") as fl:
    count = 0
    for phrase in fl:
        if check_passphrase(phrase):
            count += 1

    print count
