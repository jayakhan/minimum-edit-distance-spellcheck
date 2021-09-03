import re
from test import correct
import numpy as np

#Edit Distance Function
def edit_distance(word):
    pass    

def update_text_file(text_file):
    with open(text_file, 'r') as f:
        updated_list = []
        pattern = r'[^a-zA-Z0-9]'
        reg = re.compile('[\w]{2,}')
        list_words = ([word for line in f for word in line.split(' ')])
        np_array = np.array(list_words)
        for word in np_array:
            #Pick word from dictionary
            updated_word = edit_distance(re.sub(pattern, '', word))
            print(updated_word)
            #Detokenize word
            updated_list.append(reg.sub(updated_word, word))
            print(updated_list)


if __name__ == '__main__':
    print(update_text_file('/Users/zayakhan/Dev/basic-spellcheck/austen-sense-corrupted.txt'))