from pip._vendor.distlib.compat import raw_input


def minion_game(string):

    vowels = set("aeiouAEIOU")
    vowel_words = []
    non_vowel_words = []
    for i in range(len(string)):
        if string[i] in vowels:
            for j in range(i, len(string)+1):
                if string[i:j] != '':
                    vowel_words.append(string[i:j])
        else:
            for j in range(i, len(string)+1):
                if string[i:j] != '':
                    non_vowel_words.append(string[i:j])

    if len(vowel_words) > len(non_vowel_words):
        print("Kevin", len(vowel_words))
    elif len(vowel_words) < len(non_vowel_words):
        print("Stuart", len(non_vowel_words))
    else:
        print("Draw")



if __name__ == '__main__':
    s = raw_input()
    minion_game(s)