"""Code for exercise 1.
Starter code by Instructor David Szeto. Implementation by the CSCA20 student.
"""


def constant_function():
    """A basic toy function which always returns 0

    Args:
        No args
    """
    # Write your code here and delete the line containing "pass"
    print(0)


def area_square(length):
    """Returns the area of a square with the given side length

    Args:
        length: a number. The length of a side of the square of interest.
    """
    # Write your code here and delete the line containing "pass"
    # length = input('Enter the length of one side')
    print(length ** 2)


def area_parallelogram(base, height):
    """Returns the area of a parallelogram.

    Returns the area of a parallelogram with the given base length and height
    according to the formula here:
    https://en.wikipedia.org/wiki/Parallelogram#Area_formula

    Args:
        base: a number. The length of the base of the parallelogram
        height: a number. The height of the parallelogram.
    """
    # Write your code here and delete the line containing "pass"
    print(base * height)


def is_string_empty(string):
    """Returns whether the given string is empty.

    Args:
        string: a str
    """
    # Write your code here and delete the line containing "pass"
    string = str(string)
    if not(bool(string)):
        print(True)
    else:
        print(False)


# do NOT modify this line! It's here to help the automarker do its job. I'll be
# explaining in lecture shortly what it does and why it's here.
if __name__ == '__main__':
    # --------------------------------------------------------------------------
    # You may use the area down here to write code in order to test whether
    # your implemented functions actually do what you want them to do. For
    # example, you may want to print many calls to each function with various
    # different argument values in order to be reasonably confident that your
    # code actually works.

    # For example, here are SOME of the tests I might personally run for the
    # function area_parallelogram. However, PLEASE WRITE YOUR OWN AS WELL! As
    # programmers, you're responsible for making sure your code does what you
    # think it should do.
    area_parallelogram(0, 0)  # should print 0
    area_parallelogram(0, 100)  # should print 0
    area_parallelogram(10, 10)  # should print 100
    area_square(4)
    is_string_empty('')
    constant_function()

    # In general, you should test your functions on many different
    # (combinations of) values. Keep in mind that we instructors will test your
    # code thoroughly, and if we find any errors, we will not accept the excuse
    # of, "I thought I tested my code and it looked like it worked".

    # Note that any code you write here must be indented by four spaces, so
    # that it belongs to the if __name__ == '__main__' block.
