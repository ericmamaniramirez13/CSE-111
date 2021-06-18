import random
def get_determiner(quantity):
    if quantity == 1:
        words = ["the", "one", "a"]
    else:
        words = ["some", "many"]
    word = random.choice(words)
    return word
def get_noun(quantity):
    if quantity == 1:
        nouns = ["adult", "bird", "boy", "car", "cat",
        "child", "dog", "girl", "man", "woman"]
    else:
        nouns = ["adults", "birds", "boys", "cars", "cats",
        "children", "dogs", "girls", "men", "women"]
    noun = random.choice(nouns)
    return noun
def get_verb(quantity, tense):
    if tense == "past":
        verbs = ["drank", "ate", "grew", "laughed", "thought",
    "ran", "slept", "talked", "walked", "wrote"]
    elif tense == "present" and quantity == 1:
        verbs = ["drinks", "eats", "grows", "laughs", "thinks",
    "runs", "sleeps", "talks", "walks", "writes"]
    elif tense=="present" and quantity !=1:
        verbs = ["drink", "eat", "grow", "laugh", "think",
        "run", "sleep", "talk", "walk", "write"]
    elif tense =="future":
        verbs = ["will drink", "will eat", "will grow", "will laugh",
        "will think", "will run", "will sleep", "will talk",
        "will walk", "will write"]
    verb = random.choice(verbs)
    return verb
def get_preposition():
    prepositions = ["about", "above", "across", "after", "along",
        "around", "at", "before", "behind", "below",
        "beyond", "by", "despite", "except", "for",
        "from", "in", "into", "near", "of",
        "off", "on", "onto", "out", "over",
        "past", "to", "under", "with", "without"]
    preposition = random.choice(prepositions)
    return preposition
def get_prepositional_phrase(quantity,tense):
    prepositional_phrase=[]
    prepositional_phrase.append(get_determiner(quantity))
    prepositional_phrase.append(get_noun(quantity))
    prepositional_phrase.append(get_verb(quantity,tense))
    prepositional_phrase.append(get_preposition())
    prepositional_phrase.append(get_determiner(quantity))
    prepositional_phrase.append(get_noun(quantity))
    return prepositional_phrase
def main():
    for y in range(0,2):    
        for i in range (1,7):
            sentence=[]
            if i%2==1:
                x=1
                #print(x)
            else:
                x=2
                #print(x)
            if i<3:
                tense="past"
                #print(tense)
            elif i >2 and i<5:
                tense="present"
                #print(tense)
            else:
                tense="future"
                #print(tense)
            if y == 0:
                sentence.append(get_determiner(x))
                sentence.append(get_noun(x))
                sentence.append(get_verb(x,tense))
                for words in sentence:
                    print(words, end=" ")
                print("")
            if y ==1:
                for words in get_prepositional_phrase(x, tense):
                    print(words, end=" ")
                print("")
main()