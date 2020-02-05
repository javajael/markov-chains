"""Generate Markov text from text files."""

from random import choice
import sys


def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    # your code goes here

    input_file = open(file_path)
    read_data = input_file.read()

    # print(read_data)
    #  close the file!!!
    return read_data


def make_chains(text_string):
    """Take input text as string; return dictionary of Markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> chains = make_chains("hi there mary hi there juanita")

    Each bigram (except the last) will be a key in chains:

        >>> sorted(chains.keys())
        [('hi', 'there'), ('mary', 'hi'), ('there', 'mary')]

    Each item in chains is a list of all possible following words:

        >>> chains[('hi', 'there')]
        ['mary', 'juanita']
        >>> chains[('there','juanita')]
        [None]
    """

    chains = {}

    # your code goes here
    text_string = text_string.split()
    # print("text_string after split", text_string)

    for i in range(len(text_string)-1):
        # print(text_string[i], text_string[i+1])

        if i+2 <= len(text_string)-1:
            # make bigram variable,make it a tuple and assign word at i and i+1
            bigram = (text_string[i], text_string[i+1])
            # bv = get bigram value from chains, if not there,
            # assign empty list to value
            bigram_value = chains.get(bigram, [])
            # bv is now a value, or an empty list.
            # append to that [] text_string[i+2]
            bigram_value.append(text_string[i+2])
            # set the value of bigram in chains
            chains[bigram] = bigram_value

    # print("Chains dictionary", chains)

    return chains


def make_n_gram_chain(text_string, n):
    # right now this is written as if n is 3 - will need to substitute
    # indexing to accomodate n values
    chains = {}
    text_string = text_string.split()
    for i in range(len(text_string)-2):
        if i+3 <= len(text_string)-2:
            n_gram = (text_string[i], text_string[i+1], text_string[i+2])
            n_gram_value = chains.get(n_gram)
            # use list splicing instead?
            print("text_string[i+3]=", text_string[i+3])
            if text_string[i+3] is not None:
                n_gram_value.append(text_string[i+3])
                chains[n_gram] = n_gram_value
            else:
                break
    return chains


def make_text(chains):
    """Return text from chains."""
    words = []
    # keys = chains.keys()

    # your code goes here
    # for bigram, words in chains.items():
    #     # print("print1",bigram, words)
    #     print("bigram", bigram[1])

    # Make an initial link
    initial_key = choice(list(chains.keys()))
    # print("Initial key = ", initial_key)

    words = [initial_key[0], initial_key[1]]
    # print("words[] = ", words)

    initial_key_value = chains.get(initial_key)
    # print("initial_key_value", initial_key_value)

    random_next_word = choice(initial_key_value)
    # print("random_next_word", random_next_word)

    # link = (initial_key, random_next_word)
    # print("link", link)

    while random_next_word is not None:
        # get the second indeces of initial_key put it at the
        # first index of key
        initial_key = (initial_key[1], random_next_word)
        # print("initial_key", initial_key)
        words.append(random_next_word)
        # print("chains.get(key)", chains.get(key))
        if chains.get(initial_key) is None:
            break
        else:
            random_next_word = choice(chains.get(initial_key, []))
            # print("Random_next word is now = ", random_next_word)
    # Look up the value for that link in our chain
    # choose random word from the list (value associated to that key)
    # make next link using word2 from the key of the previous link,

    return " ".join(words)


def make_text_from_n_gram(chains):
    words = []

    key = choice(list(chains.keys()))
    # for n grams - loop over a range of indices? so  for i in range(n)...
    word1 = key[0]
    word2 = key[1]
    word3 = key[2]

    words = [word1, word2, word3]
    # debug print
    print(words)

    new_word = choice(chains.get(key))

    while new_word is not None:
        key = (word1, word2, new_word)
        words.append(new_word)
        if chains.get(key) is None:
            break
        else:
            new_word = choice(chains.get(key, []))

    return " ".join(words)



# input_path = "green-eggs.txt"
# take  the file passed in as a command line argument, and set that
# as the file path/file name to use for our input

input_path = sys.argv[1]

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print(random_text)

# try out our n-gram version
chains = make_n_gram_chain(input_text, 3)
random_text = make_text_from_n_gram(chains)

