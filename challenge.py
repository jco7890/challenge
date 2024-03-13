#1 - Add a prefix to word
def add_prefix_un(word):
    return "un"+word
word = input("enter word to make negative: ")
print(add_prefix_un(word))

#2 - Add prefixes to word groups
def make_word_groups(vocab_words):
    prefix = vocab_words[0]
    words_after_prefix = vocab_words[1:]
    new_words = [prefix+word for word in words_after_prefix]
    return "::".join([prefix]+new_words)

pre_processed_list = input("write list of words with prefix at start: ")
vocab_words = pre_processed_list.split()
new_list = make_word_groups(vocab_words)
print(new_list)

#3 - Remove a suffix from a word
def remove_suffix_ness(input_word):
    if input_word.endswith("iness"):
        new_word = input_word[:-5]+"y"
        return new_word
    elif input_word.endswith("ness"):
        new_word = input_word[:-4]
        return new_word
    else:
        return input_word

input_word = input("enter word to remove suffix from: ")
new_word = remove_suffix_ness(input_word)
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









