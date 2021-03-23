def int_func_all(*words):
    words = list(words)
    for word in words:
        yield word.title()


def int_func(word):
    return word.title()


def int_func_from(*words):
    yield from (word.title() for word in words)


if __name__ == '__main__':
    words = input('Enter words, using space: ').split()
    word_str = ' '.join(list(int_func_all(*words)))
    word_str_fr = ' '.join(list(int_func_from(*words)))
    new_word = ' '.join(list(map(lambda word: int_func(word), words)))
    print('\tYour new string is: %s' % word_str)
    print('\tYour new string is: [%s = %s]' % (word_str, word_str_fr))  # output of two equal functions
    print('\tFirst version of int_func(): %s' % new_word)