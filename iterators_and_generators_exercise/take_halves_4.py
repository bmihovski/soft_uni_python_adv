def solution():
    def integers():
        start = 1
        while True:
            yield start
            start += 1

    def halves():
        for i in integers():
            start = i / 2
            yield start

    def take(n, seq):
        results = list()
        for j in seq:
            if len(results) == n:
                break
            results.append(j)
        return results

    return take, halves, integers


from unittest import TestCase


class TakeHalvesTests(TestCase):
    def test_zero(self):
        take = solution()[0]
        halves = solution()[1]
        self.assertEqual([0.5, 1.0, 1.5, 2.0, 2.5], take(5, halves()))
