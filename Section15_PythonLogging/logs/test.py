from logger import logging

def add(a,b):
  logging.debug("Addition Function is called")
  return a+b

add(10,5)
logging.debug("Addition Function Successful")