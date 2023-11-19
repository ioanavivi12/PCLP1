# import functions from other files
import ctypes
from ctypes import *
import os

def main():
    os.system("make")
    hidden_main = ctypes.CDLL("checker/hidden.so")
    hidden_message = hidden_main.get_hidden_message()

    user_main = ctypes.CDLL("./user.so")
    user_message = user_main.decript_message(hidden_message, 20)

    hidden_main.check_hidden_message(user_message)


if __name__ == '__main__':
    main()