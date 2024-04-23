import random

def shuffle_word(word):
    if len(word) <= 3:
        return word
    
    first_letter = word[0]
    last_letter = word[-1]
    middle_part = list(word[1:-1])
    random.shuffle(middle_part)
    shuffled_word = first_letter + ''.join(middle_part) + last_letter
    
    return shuffled_word

def shuffle_sentence(sentence):
    words = sentence.split()
    shuffled_words = [shuffle_word(word) for word in words]
    shuffled_sentence = ' '.join(shuffled_words)
    
    return shuffled_sentence

print(shuffle_sentence('hello'))