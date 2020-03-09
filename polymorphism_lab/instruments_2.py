class Guitar:
    def play(self):
        return "playing the guitar"


class Piano:
    def play(self):
        return "pianoto"


def play_instrument(obj: object):
    return obj.play()


from unittest import TestCase


class InstrumentsTests(TestCase):


    def test_guitar(self):
        guitar: Guitar = Guitar()
        self.assertEqual("playing the guitar", play_instrument(guitar))

    def test_piano(self):
        piano: Piano = Piano()
        self.assertEqual("pianoto", play_instrument(piano))

if __name__ == 'main':
    TestCase.main()