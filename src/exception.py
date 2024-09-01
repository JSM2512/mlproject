## I will write custom exceptions

import sys
from src.logger import *

def error_message_detail(error, error_detail:sys):
    _,_,exec_tb = error_detail.exc_info() ## exec_tb will give details of errors with line numbers
    file_name = exec_tb.tb_frame.f_code.co_filename
    error_message = "Error occured in python script name [{0}] line number [{1}] error message [{2}]".format(
        file_name, exec_tb.tb_lineno, str(error))
    
    return error_message


class CustomException(Exception):                           ## CustomException inherits Exception Class
    def __init__(self, error_message, error_detail:sys):    ## Constructor with error_message and error_detail parameters
        super().__init__(error_message)                       ## Call the superclass (Exception) constructor
        self.error_message = error_message_detail(error_message, error_detail=error_detail)

    def __str__(self):
        return self.error_message
    

# if __name__=="__main__":
#     try:
#         a = 1/0
#         print("hello")
#     except Exception as e:
#         logging.info("Exception is raised for divide by 0")
#         raise CustomException(e,sys)
        




