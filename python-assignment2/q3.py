"""
Write code that will print out the anagrams (words that use the same
letters) from a paragraph of text.
"""


def find_anagrams(sample_input):
    """
    function to return the list of anagram word from the given sentence
    :param sample_input: sample list of word
    :return: list of anagram word
    """
    split_word = sample_input.split(' ')
    result = []
    for i in split_word:
        for j in split_word:
            if i != j:
                if sorted(i) == sorted(j):
                    if i not in result:
                        result.append(i)
                    if j not in result:
                        result.append(j)

    if result:
        return result
    else:
        return "No Anagrams Word"


if __name__ == "__main__":
    sample_sentence = "ram mar show do od"
    result = find_anagrams(sample_sentence)
    print(result)
