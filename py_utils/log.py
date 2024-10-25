import logging
from typing import Type, Union

def getCustomLogger(logger_name_   : str,
                    node_name_     : str,
                    log_handler_   : Type[Union[logging.StreamHandler, logging.FileHandler]],
                    logging_level_ : int):
    """
    Create and return a properly formatted Logger object associated with the given log handler.
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
