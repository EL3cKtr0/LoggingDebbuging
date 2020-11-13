import logging
filename = 'Debug.txt'

# create logger
logger = logging.getLogger('LogExample')
logger.setLevel(logging.DEBUG)

#create file
file = logging.FileHandler(filename)
file.setLevel(logging.DEBUG)
logger.addHandler(file)

# create formatter
formatter = logging.Formatter()
file.setFormatter(formatter)
logger.addHandler(file)

# 'application' code
logger.debug('Debug')
logger.info('Info')
logger.warning('Warning')
logger.error('Error')
logger.critical('Critical Error')
