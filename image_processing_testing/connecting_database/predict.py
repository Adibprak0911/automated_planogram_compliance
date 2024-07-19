import database_interaction

all_words = database_interaction.get_all_words()

# all_words = {'at', 'cat', 'bat', 'hat', 'rat', 'sprite'}
def expand_phrases(word_list):
    expanded_words = set()

    for phrase in word_list:
        words = phrase.split()
        expanded_words.update(words)  # Add individual words to the set
        expanded_words.add(phrase)    # Add the original phrase to the set

    return list(expanded_words)

# Example usage
words = ["hello world"]
all_words = expand_phrases(all_words)

def edits_one(word):
    "all edits that are one edit away from word"
    alphabets = 'abcdefghijklmnopqrstuvwxyz'
    splits     = [(word[:i], word[i:])                   for i in range(len(word) + 1)]
    deletes    = [left + right[1:]                       for left, right in splits if right]
    inserts    = [left + c + right                       for left, right in splits for c in alphabets]
    replaces   = [left + c + right[1:]                   for left, right in splits if right for c in alphabets]
    transposes = [left + right[1] + right[0] + right[2:] for left, right in splits if len(right)>1]
    return set(deletes + inserts + replaces + transposes)
    

def edits_two(word):
    "all edits that are two edits away from word"
    return(e2 for e1 in edits_one(word) for e2 in edits_one(e1))

def known(words):
    return set(word for word in words if word in all_words)

# print(known("cat"))

def possible_corrections(word):
    "generate possible spelling corrections for word"
    return list((known([word]) or known(edits_one(word)) or known(edits_two(word)) or [word]))

# print(possible_corrections("chilli chka"))

