def tags(tag: str):
    def decorator(func):
        def wrapper(*args):
            return f"<{tag}>{func(*args)}</{tag}>"
        return wrapper
    return decorator


from unittest import TestCase


class HtmlTagsTests(TestCase):
    def test_join(self):
        @tags('p')
        def join_strings(*args):
            return "".join(args)
        self.assertEqual("<p>Hello you!</p>", join_strings("Hello", " you!"))

    def test_upper(self):
        @tags('h1')
        def to_upper(text):
            return text.upper()
        self.assertEqual("<h1>HELLO</h1>", to_upper('hello'))
