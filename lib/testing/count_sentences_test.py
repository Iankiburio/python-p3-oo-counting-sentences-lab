#!/usr/bin/env python3

from count_sentences import MyString

import io
import sys
class TestMyString:
    def test_is_class(self):
        string = MyString("")
        assert type(string) == MyString

    def test_value_string(self):
        captured_out = io.StringIO()
        sys.stdout = captured_out
        string = MyString(123)
        sys.stdout = sys.__stdout__
        assert captured_out.getvalue() == "The value must be a string.\n"

    def test_is_sentence(self):
        assert MyString("Hello World.").is_sentence() is True
        assert MyString("Hello World").is_sentence() is False

    def test_is_question(self):
        assert MyString("Is anybody there?").is_question() is True
        assert MyString("Is anybody there").is_question() is False

    def test_is_exclamation(self):
        assert MyString("It's me!").is_exclamation() is True
        assert MyString("It's me").is_exclamation() is False

    def test_count_sentences(self):
        simple_string = MyString("one. two. three?")
        empty_string = MyString("")
        complex_string = MyString("This, well, is a sentence. This is too!! And so is this, I think? Woo...")
        assert simple_string.count_sentences() == 3
        assert empty_string.count_sentences() == 0
        assert complex_string.count_sentences() == 4