import re
#Global variables
list_dict_words = []
edit_distance_dict = {}

#Initialize Dictionary words
def initialize_dictionary(dictionary):
    with open(dictionary, 'r') as f:
        for word in f:
            list_dict_words.append(word.strip('\n'))

#Find minimum edit distance
def compute_edit_distance(source_word, target_word):
    n = len(source_word)
    m = len(target_word)
    distance = [[0 for x in range(m+1)] for y in range(n+1)]
    distance[0][0] = 0
    for i in range(1, n+1):
        distance[i][0] = distance[i-1][0] + 1
    for j in range(1, m+1):
        distance[0][j] = distance[0][j-1] + 1
    for a in range(1, n+1):
        for b in range(1, m+1):
            distance[a][b] = min(distance[a-1][b] + 1, (distance[a-1][b-1] + 0 if source_word[a-1] == target_word[b-1] else distance[a-1][b-1] + 2), distance[a][b-1] + 1)
    return distance[n][m]

#Return word with min edit distance
def edit_distance(word):
    if word not in list_dict_words:
        for dict_word in list_dict_words:
            dist = compute_edit_distance(word, dict_word) 
            edit_distance_dict[dict_word] = dist
        word = min(edit_distance_dict, key=edit_distance_dict.get)
    return word

#Main function
def update_text_file(text_file):
    str = ''
    initialize_dictionary('/Users/zayakhan/Dev/basic-spellcheck/google-10000-english.txt')
    with open(text_file, 'r') as f:
        update_list = []
        pattern = r'[^a-zA-Z0-9]'
        reg = re.compile('[\w]{1,}')
        list_words = ([word for line in f for word in line.split(' ')])
        for word in list_words:
            if not word or word != ' ':
                if word != '\n': 
                    #Pick word from dictionary
                    substring = re.sub(pattern, '', word)
                    found_word = edit_distance(substring.lower())
                    #Detokenize word
                    update_list.append(reg.sub(found_word, word))
                else:
                    update_list.append('\n')
            else:
                update_list.append(' ')      
        for element in update_list:
            str += element + ' '
        return str
        
        '''
        Code for writing string to file
        textfile = open("new_file.txt", "w")
        for element in update_list:
            textfile.write(element + ' ')
        textfile.close()     
        ''' 

if __name__ == '__main__':
    update_text_file('/Users/zayakhan/Dev/basic-spellcheck/austen-sense-corrupted.txt')