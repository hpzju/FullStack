import string

if __name__ == "__main__":
    source_str = my_story = """ 2 Pythons are constrictors, which means that they will 'squeeze' the life 3 out of their prey. They coil themselves around their prey and with 4 each breath the creature takes the snake will squeeze a little tighter 5 until they stop breathing completely. Once the heart stops the prey 6 is swallowed whole. The entire animal is digested in the snake's 7 stomach except for fur or feathers. What do you think happens to the fur, 8 feathers, beaks, and eggshells? The 'extra stuff' gets passed out as --9 you guessed it --- snake POOP! """
    filtered = filter(lambda c: c not in string.punctuation, source_str)
    print("".join(filtered))
