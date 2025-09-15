import logging
from typing import Union

def getCustomLogger(logger_name_  : str,
                    node_name_    : str,
                    log_handler_  : Union[logging.StreamHandler, logging.FileHandler],
                    logging_level_: int) -> logging.Logger:
    """
    Create and return a properly formatted Logger object associated with the given log handler.

    Args:
        logger_name_ (str): Name of the logger.
        node_name_ (str): Node/module name to include in log messages.
        log_handler_ (Union[logging.StreamHandler, logging.FileHandler]): 
            A logging handler instance (e.g., logging.StreamHandler() or logging.FileHandler(...)).
        logging_level_ (int): Logging level (e.g., logging.INFO).

    Returns:
        logging.Logger: Configured logger instance.
    """

    logger = logging.getLogger(logger_name_)
    logger.setLevel(logging_level_)

    logger.addHandler(log_handler_)
    logger.propagate = False # Don't send logs to the root loggers handlers
    
    log_formatter = logging.Formatter(
        fmt="[%(asctime)s.%(msecs)03d][%(levelname)s][" + node_name_ + "]: %(message)s",
        datefmt="%Y-%m-%d,%H:%M:%S"
    )
    log_handler_.setFormatter(log_formatter)

    return logger

##### ----- Test Script ----- #####

def test():
    ## Test 1 - Check that the function works
    logger = getCustomLogger(logger_name_=__name__,
                             node_name_="First Node",
                             log_handler_=logging.StreamHandler(),
                             logging_level_=logging.INFO)
    
    logger.info("First call")
    ## Test 1 - End

if __name__ == "__main__":
    test()
