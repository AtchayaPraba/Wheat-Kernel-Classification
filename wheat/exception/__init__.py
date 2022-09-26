import sys

# Create coustome exception class
class WheatException(Exception):
    
    def __init__(
        self, 
        error_message:Exception, 
        error_detail:sys
    ):
        super().__init__(error_message)
        self.error_message = WheatException.get_detailed_error_message(
            error_message=error_message,
            error_detail=error_detail
        )

    # Independent function within WheatException class
    @staticmethod
    def get_detailed_error_message(
        error_message:Exception, 
        error_detail:sys
    ) -> str:
        """
        error_message: Form Exception 
        error_detail: From sys module
        """
        # Get exec_tb from error_detail i.e sys
        _,_,exec_tb = error_detail.exc_info()
        # Get exception_block_line_number, try_block_line_number and file_name from exec_tb
        exception_block_line_number = exec_tb.tb_frame.f_lineno
        try_block_line_number = exec_tb.tb_lineno
        file_name = exec_tb.tb_frame.f_code.co_filename

        error_message = f"""Error occured in script: [ {file_name} ] at
                            try block line number: [{try_block_line_number}] and exception block line number: [{exception_block_line_number}]
                            error message: [{error_message}]
                            """
        return error_message

    def __str__(self):
        return self.error_message

    def __repr__(self) -> str:
        return WheatException.__name__.str()