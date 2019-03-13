import logging
import pdb

"""
This is a logigng and python debugger test
possible use of pdb is
import pdb; pdb.set_trace()
"""

logging.basicConfig(filename='game.log', level=logging.DEBUG)

my_list = [1,'two',[3]]

pdb.set_trace()

logging.info(my_list)
del my_list[0]

print(my_list)

logging.info(my_list)
del my_list[-1]

print(my_list)

print("end")
