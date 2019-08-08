"""Build a pyramid from characters in a given string."""

def watch_pyramid_from_the_side(characters):
    """."""
    characters.split()
    characters.reverse()
    size = len(characters)
    multiplier = 0
    big_string = ""
    for i in characters:
        big_string += " " * size - 1
        big_string += i * ((multiplier * 2) + 1)
        big_string += " " * size - 1
        big_string += "/n"
        size += -1
        multiplier += 1

def watch_pyramid_from_above(characters):
    characters.split()
    characters.reverse()
    size = len(characters)

def count_visible_characters_of_the_pyramid(characters):

def count_all_characters_of_the_pyramid(characters):
