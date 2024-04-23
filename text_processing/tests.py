from django.test import TestCase
from .utils import shuffle_word, shuffle_sentence
from collections import Counter

class TextProcessingTests(TestCase):
    def test_shuffle_word(self):
        self.assertEqual(shuffle_word("a"), "a")
        self.assertEqual(shuffle_word("abc"), "abc")
        word = "encyclopedia"
        self.assertNotEqual(shuffle_word(word), word)
        self.assertEqual(shuffle_word(word)[0], word[0])
        self.assertEqual(shuffle_word(word)[-1], word[-1])
        self.assertEqual(Counter(shuffle_word(word)), Counter(word))

    def test_shuffle_sentence(self):
        self.assertEqual(shuffle_sentence(""), "")
        self.assertEqual(shuffle_sentence("set"), "set")
        sentence = "This is an example sentence."
        self.assertNotEqual(shuffle_sentence(sentence), sentence)
        self.assertEqual(Counter(shuffle_sentence(sentence)), Counter(sentence))
