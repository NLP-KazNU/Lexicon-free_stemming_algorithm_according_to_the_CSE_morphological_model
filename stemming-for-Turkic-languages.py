import re

def splitting_by_words(text):
    result = re.findall(r'\w+', text)
    return result

def sorting_affixes(file_name):
    affixes_file = open(file_name, 'r', encoding="utf-8")
    affixes_file = affixes_file.read()

    affixes = splitting_by_words(affixes_file.lower())

    sorted_affixes = sorted(affixes, key=len, reverse=True)

    return sorted_affixes

def stem(word, affixes):
    word_len = len(word)
    min_len_of_word = 2
    stems = []

    if word_len > min_len_of_word:
            n = word_len - min_len_of_word
            for i in range(n+1, 0, -1):
                word_affix = word[word_len - (i-1):]
                stem = word[:word_len-len(word_affix)]
                for affix in affixes:
                    if affix == word_affix:
                        stems.append(stem)
                    elif affix == '' or word_affix == '':
                        stems.append(word)
                        
    return stems[0]
    

def stemming(file_name, affixes):
    text_file = open(file_name, 'r', encoding="utf-8")
    text_file = text_file.read()

    text = splitting_by_words(text_file)
    res_text = []
    for word in text:
        if word not in res_text:
            res_text.append(word)

    stem_text = {}
    for word in res_text:
        stemm = stem(word, affixes)
        stem_text.update({word: stemm})

    for i in stem_text.keys():
        word = str(i)
        stemm = str(stem_text[i])

        if word in text_file:
            text_file = re.sub((rf"\b{word}\b"), stemm, text_file)
       
    return text_file
    

affixes_file_name = "affixes.txt"
affixes = sorting_affixes(affixes_file_name)
print(affixes)

text_file_name = "text.txt"
text = stemming(text_file_name, affixes)
print("\n")
print(text)

output_file_name = "results.txt"
output_file = open(output_file_name, 'w', encoding="utf-8")
output_file.write(text)
output_file.close()


