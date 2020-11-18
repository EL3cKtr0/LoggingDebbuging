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
    if (l1 + l2) < l3:
        logger.error("ERROR, third number is bigger than the sum other two")
        return True
    if (l1 + l3) < l2:
        logger.error("ERROR, second number is bigger than the sum other two")
        return True
    if (l2 + l3) < l1:
        logger.error("ERROR, first number is bigger than the sum other two")
        return True

    return False


def test_method():
    first = input()
    if not first.isdigit():
        logger.error('ERROR, first number must be a digit!')
    assert first.isdigit() == True
    second = input()
    if not second.isdigit():
        logger.error('ERROR, second number must be a digit!')
    assert second.isdigit() == True
    third = input()
    if not third.isdigit():
        logger.error('ERROR, third number must be a digit!')
    assert third.isdigit() == True

    logger.debug("All 3 numbers are valid for testing")
    assert istriangle(int(first), int(second), int(third)) == False
    logger.debug("The 3 Numbers can be 3 sides of a triangle")
