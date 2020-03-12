def vowel_filter(function):
    def wrapper():
        vowels_to_filter = function()
        filtered_vowels = list(filter(lambda vowel: vowel.lower() in ['a', 'e', 'i', 'u', 'o', 'y'], vowels_to_filter))
        return filtered_vowels
    return wrapper


from unittest import TestCase


class VowelFilterTests(TestCase):
    def test_zero(self):
        @vowel_filter
        def get_letters():
            return ["a", "b", "c", "d", "e"]

        self.assertEqual(['a', 'e'], get_letters())
