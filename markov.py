#! /usr/bin/env python3

import collections
import random
import re

#
# Exercise 13.8. Markov Analysis
#

text = """Half a bee, philosophically, 
Must, ipso facto, half not be. 
But half the bee has got to be 
Vis a vis, its entity. D’you see?
But can a bee be said to be
Or not to be an entire bee 
When half the bee is not a bee 
Due to some ancient injury?"""


def markov_analysis(text, prefix_length):
    #print(text)

    words = re.split(r"[^a-zA-Z]+", text)
    words = filter(None, words)
    words = list(map((lambda w: w.lower()), words))

    #print(words)

    ngrams = [words[i:i + prefix_length + 1] for i in range(0, len(words) - prefix_length)]

    #print(ngrams)

    result = collections.defaultdict(list)

    for ngram in ngrams:
        prefix = tuple(ngram[:prefix_length])
        suffix = ngram[prefix_length]

        result[prefix].append(suffix)
    
    for prefix, suffixes in result.items():
        print("{} -> {}".format(prefix, suffixes))

    return dict(result)


def random_prefix_list(markov_dict):
    return list(random.choice(list(markov_dict.keys())))


def random_markov_text(markov_dict, length):

    text_list = random_prefix_list(markov_dict)
    prefix_length = len(text_list)

    while length - len(text_list) > 0:

        prefix = tuple(text_list[-prefix_length:])

        if not prefix in markov_dict:
            text_list.append(".\n\n") 
            prefix = random_prefix_list(markov_dict)
        
        suffixes = markov_dict[prefix]
        next_word = random.choice(suffixes)
        text_list.append(next_word)

    return " ".join(text_list)


if __name__ == "__main__":
    
    with open('./emma.txt', 'r') as file:
        text = file.read()
        
    markov_dict = markov_analysis(text, 5)
    random_text = random_markov_text(markov_dict, 10000)

    print(random_text)
