import logging
import os

def setup_logging(log_file_path='logs/logging.log'):
    """
    Set up logging configuration with both file and console handlers.

    :param log_file_path: Path to the log file.
    :return: Configured logger.
    """
    # Ensure the directory for log files exists
    os.makedirs(os.path.dirname(log_file_path), exist_ok=True)

    # Clear any previous logs in the file
    with open(log_file_path, 'w'):
        pass

    # Create a logger
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)  # Set the overall logger level

    # Create handlers
    file_handler = logging.FileHandler(log_file_path)  # Logs to a file
    console_handler = logging.StreamHandler()  # Logs to the console

    # Set level for handlers
    file_handler.setLevel(logging.DEBUG)
    console_handler.setLevel(logging.INFO)

    # Create formatters and add them to the handlers
    file_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    console_format = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(file_format)
    console_handler.setFormatter(console_format)

    # Add the handlers to the logger
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger
