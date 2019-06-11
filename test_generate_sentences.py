import pytest
from generate_sentences import *

sentences0 = ["Henry", "Amy"]
sentences1 = ["John", "Mary"]
sentences2 = ["John", "Bob", "Diana"]
sentences3 = ["Brian", "Sean", "Vlad", "Johnny"]

predicates0 = ["eats"]
predicates1 = ["hates", "loves"]
predicates2 = ["drives"]
predicates3 = ["drinks", "sips"]

objects0 = ["pizza", "kebab"]
objects1 = ["apples", "bananas"]
objects2 = ["a car", "a motorcycle", "a bus"]
objects3 = ["whiskey"]


def test_generate_sentence():

    assert generate_sentence(sentences0, predicates0, objects0) == "Amy eats kebab. Amy eats pizza. " \
                                                                   "Henry eats kebab. Henry eats pizza. "

    assert generate_sentence(sentences1, predicates1, objects1) == "John hates apples. John hates bananas. " \
                                                                   "John loves apples. John loves bananas. " \
                                                                   "Mary hates apples. Mary hates bananas. " \
                                                                   "Mary loves apples. Mary loves bananas. "

    assert generate_sentence(sentences2, predicates2, objects2) == "Bob drives a bus. Bob drives a car. " \
                                                                   "Bob drives a motorcycle. Diana drives a bus. " \
                                                                   "Diana drives a car. Diana drives a motorcycle. " \
                                                                   "John drives a bus. John drives a car. " \
                                                                   "John drives a motorcycle. "

    assert generate_sentence(sentences3, predicates3, objects3) == "Brian drinks whiskey. Brian sips whiskey. " \
                                                                   "Johnny drinks whiskey. Johnny sips whiskey. " \
                                                                   "Sean drinks whiskey. Sean sips whiskey. " \
                                                                   "Vlad drinks whiskey. Vlad sips whiskey. "
