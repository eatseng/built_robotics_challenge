import sys

# sys.argv[1] - file name

# sys.argv[2] - user anagram input

r = ord('z')


def reset_cache(cache):

    for key in range(ord('a'), r + 1):

        cache[key] = 0

    return cache


def sort_string(string, cache):

    # We use radix sort to sort string characters in R * len(string) run time

    buffer = []

    reset_cache(word_cache)

    for char in string.lower():

        key = ord(char)

        cache[key] += 1

    for key in range(ord('a'), r + 1):

        for i in range(cache[key]):

            buffer.append(chr(key))

    return "".join(buffer)


def get_subset_without_dup(chars):

    # 1. We create subset by continuously appending new char with existing

    # elements in the subset, creating a new subset while also preserving the

    # original subset.

    # 2. We avoid creating duplicates by counting the number of repeating chars

    # and creating subset of identical char array of k size (where k is the

    # number of repeats) and append them using #1 algorithm

    subset, cache = [[]], {}

    for char in chars:

        if char not in cache:

            cache[char] = 0

        cache[char] += 1

    for key in cache:

        copy_subset = [item for item in subset]

        repeats = [[key for i in range(n + 1)] for n in range(cache[key])]

        for intermediate in repeats:

            subset += [copy + intermediate for copy in copy_subset]

    return subset


if __name__ == '__main__':

    all_words_cache, word_cache = {}, [0 for i in range(r + 1)]

    # Create word anagram look up

    with open(sys.argv[1], encoding="utf-8") as f:

        for line in f:

            word = line.rstrip()

            anagram = sort_string(word, word_cache)

            if anagram not in all_words_cache:

                all_words_cache[anagram] = []

            all_words_cache[anagram].append(word)

    # Get all sub-anagram of user input word

    user_input_anagram = sort_string(sys.argv[2], word_cache)

    for subset_anagram in get_subset_without_dup(user_input_anagram):

        anagram = ''.join(subset_anagram)

        if len(anagram) > 0 and anagram in all_words_cache:

            for word in all_words_cache[anagram]:

                print(word)
