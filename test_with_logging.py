import logging
import os

filename = 'log.txt'
actualpath = os.getcwd()

# create logger
logger = logging.getLogger(actualpath)
logger.setLevel(logging.DEBUG)

# create file
file = logging.FileHandler(filename)
file.setLevel(logging.DEBUG)
logger.addHandler(file)

# create formatter
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file.setFormatter(formatter)
logger.addHandler(file)


def istriangle(l1, l2, l3):
    if isinstance(l1, str):
        logger.error("ERROR, first number is NOT a number")
        return False

    if isinstance(l2, str):
        logger.error("ERROR, second number is NOT a number")
        return False

    if isinstance(l3, str):
        logger.error("ERROR, third number is NOT a number")
        return False

    if l1 <= 0:
        logger.error("ERROR, first number is less than 0")
        return False

    if l2 <= 0:
        logger.error("ERROR, second number is less than 0")
        return False

    if l3 <= 0:
        logger.error("ERROR, third number is less than 0")
        return False

    if (l1 + l2) <= l3:
        logger.error("ERROR, third number is bigger than the sum other two")
        return False
    if (l1 + l3) <= l2:
        logger.error("ERROR, second number is bigger than the sum other two")
        return False
    if (l2 + l3) <= l1:
        logger.error("ERROR, first number is bigger than the sum other two")
        return False

    return True


def test_method():
    assert istriangle(3, 4, 7) == False  # Should return False, this is NOT a Triangle
    assert istriangle(5, 5, 5) == True  # Should return True, this is a Triangle
    assert istriangle(0, 0, 0) == False  # Should return False, can't be a Triangle
    assert istriangle('ciao', 4, 7) == False  # Should return False, passing a string
    assert istriangle(-2, 1, 1) == False  # Should return False, one side is negative
    assert istriangle(2, 1, -1) == False  # Should return False, one side is negative
    assert istriangle(-5, -5, -5) == False  # Should return False, all 3 numbers are negative
