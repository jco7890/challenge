#1 - Add a prefix to word
def add_prefix_un(word):
    return "un"+word
word = input("enter word: ")
print(add_prefix_un(word))

#2 - Add prefixes to word groups
def make_word_groups(vocab_words):
    prefix = vocab_words[0]
    other_words = vocab_words[1:]
    new_words = [prefix+word for word in other_words]
    return "::".join([prefix]+new_words)

list = input("write list of words with prefix at start: ")
vocab_words = list.split()
new_list = make_word_groups(vocab_words)
print(new_list)

#3 - Remove a suffix from a word
def remove_suffix_ness(word1):
    if word1.endswith("iness"):
        new_word = word1[:-5]+"y"
        return new_word
    elif word1.endswith("ness"):
        new_word = word1[:-4]
        return new_word
    else:
        return word

word1 = input("enter word: ")
new_word = remove_suffix_ness(word1)
print(new_word)

#4 - Extract and transform a word
def adjective_to_verb(sentence, index):
    word_list = sentence.split()
    adjective = word_list[index]
    verb = adjective + "en"
    return verb

sentence = input("enter sentence: ") 
index = int(input("enter position of word in sentence where adjective is: "))
verb = adjective_to_verb(sentence,index)
print(verb)









