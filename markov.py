"""Generate Markov text from text files."""

from random import choice


def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    # your code goes here

    input_file = open(file_path)
    read_data = input_file.read()

    print(read_data)    

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
    #print("text_string after split", text_string)
    values = []

    for i in range(len(text_string)-1):
        # print(text_string[i], text_string[i+1])
        print("i = ", i)
        print(len(text_string))

        
        if i+2 <= len(text_string)-1:
            bigram = (text_string[i], text_string[i+1])
            bigram_value = chains.get(bigram, [])
            bigram_value.append(text_string[i=2])
            chains[bigram] = bigram_value
            # if bigram in chains():
            #     chains[bigram] = values
            #     values.append(text_string[i+2])
            # else:
            #     chains[bigram, text_string[i+2]]
            # values.append(text_string[i+2])
            print("Chains dictionary", chains)
            
    return chainsls


def make_text(chains):
    """Return text from chains."""

    words = []

    # your code goes here

    return " ".join(words)


input_path = "green-eggs.txt"

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print(random_text)
