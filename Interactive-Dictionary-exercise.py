sample_dict = {
    "mouth": "Mund",
    "finger": "Finger",
    "leg": "Bein",
    "hand": "Hand",
    "face": "Gesicht",
    "nose": "Nase"
}

while True:
    word = input('Enter a word in English or EXIT: ')
    if word == 'EXIT':
        break
    if word in sample_dict:
        print('Translation: ', sample_dict[word])
    else:
        print('No match!')
print('Bye!')

