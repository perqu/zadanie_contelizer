from django.test import TestCase
from .utils import shuffle_word, shuffle_sentence
from collections import Counter

class TextProcessingTests(TestCase):

    # words
    def test_shuffle_word_single_letter(self):
        self.assertEqual(shuffle_word("a"), "a")

    def test_shuffle_word_three_letters(self):
        self.assertEqual(shuffle_word("abc"), "abc")

    def test_shuffle_word_long_word(self):
        word = "encyclopedia"
        self.assertNotEqual(shuffle_word(word), word)
        self.assertEqual(shuffle_word(word)[0], word[0])
        self.assertEqual(shuffle_word(word)[-1], word[-1])
        self.assertEqual(Counter(shuffle_word(word)), Counter(word))

    def test_shuffle_word_not_alpha(self):
        self.assertEqual(shuffle_word('123456'), '123456')

    def test_shuffle_word_with_digit(self):
        self.assertEqual(shuffle_word('alpha6'), 'alpha6')

    # sentences
    def test_shuffle_sentence_empty(self):
        self.assertEqual(shuffle_sentence(""), "")
        
    def test_shuffle_sentence_three_letters(self):
        self.assertEqual(shuffle_sentence("set"), "set")

    def test_shuffle_sentence_long_sentence(self):
        sentence = "This is an example sentence."
        shuffle = shuffle_sentence(sentence)
        self.assertNotEqual(shuffle, sentence)
        self.assertEqual(Counter(shuffle), Counter(sentence))

    def test_shuffle_sentence_with_digits(self):
        sentence = "There were 245456 cows. This is an example sentence."
        shuffle = shuffle_sentence(sentence)
        self.assertNotEqual(shuffle, sentence)
        self.assertEqual(Counter(shuffle), Counter(sentence))
        self.assertEqual(shuffle[10:17], sentence[10:17])
