
import sys
from src.logger import logging

class exception_fun(Exception):
    def __init__(self, error_details, error:sys):
        super().__init__(error_details)
        self.error_details = error_fun(error_details = error_details, error = error)

    
    def __str__(self):
        logging.info('Exception file has been executed...!')
        return self.error_details




def error_fun(error_details, error:sys):
    _,_,exc_tb = error.exc_info()
    filename = exc_tb.tb_frame.f_code.co_filename
    lineno = exc_tb.tb_lineno
    error_details = 'Error has been raised in the file : {} line number is : {} and msg is {}'.format(filename, lineno, str(error_details))
    return error_details



if __name__ =='__main__':
    try:
        x = 4
        print(x/0)
    except Exception as error:
        raise exception_fun(error, sys)
