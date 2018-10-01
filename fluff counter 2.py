exit = ''


def fluff_counter():
    """ A fun program to count the number of times a speaker says such as
    uh, oh, um, etc. in a lecture. Should run just fine in the Python Shell.

    Args: None

    Returns: None

    """

    fluff_count = 0
    count = ''
    # User will submit a blank string by pressing enter, 'end' to stop.
    while count != 'end':
        count = input('Press enter when fluff word is heard, \'end\' to stop ')
        # Adds 1 to the fluff count each time the loop runs.
        fluff_count = fluff_count + 1

    # Displays total count result
    print('\n')
    print ('There was a total of ' + str(fluff_count - 1) +
           ' fluff words heard in this session.')
    print('\n')

if __name__ == '__main__':

    # Allows for the program to repeat (such as a long lecture) or end.
    while exit != 'quit':
        fluff_counter()
        exit = input('Press Enter to continue or \'quit\' to exit. ')
        print('\n')
