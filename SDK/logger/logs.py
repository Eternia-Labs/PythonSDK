import os
import logging
import sys
from logging.handlers import TimedRotatingFileHandler

import settings


def initialize_logger() -> logging.Logger:
    """"""

    print("Initializing Logger...")

    log_name = os.getenv("LOG_NAME", "scadmin_logger")
    root_logger = logging.getLogger(log_name)

    log_level = _get_log_level_from_settings()
    root_logger.setLevel(log_level)

    log_format = os.getenv(
        "LOG_FORMAT", "[%(asctime)s] %(levelname)-4s [SC-SDK]:%(message)s"
    )
    log_date_format = os.getenv("LOG_DATE_FORMAT", "%Y-%m-%dT%H:%M:%S%z")
    log_formatter = logging.Formatter(fmt=log_format, datefmt=log_date_format)

    log_handlers_set = _get_log_handlers()

    no_of_log_handlers = len(log_handlers_set)

    if no_of_log_handlers == 1:
        log_handler = log_handlers_set.pop()
        log_handler = _set_level_and_format_in_log_handler(
            log_handler, log_formatter, log_level
        )
        root_logger.addHandler(log_handler)
        print("Initialized Logger with 1 handler")
    else:
        for log_handler in log_handlers_set:
            log_handler = _set_level_and_format_in_log_handler(
                log_handler, log_formatter, log_level
            )
            root_logger.addHandler(log_handler)
        print(f"Initialized Logger with {no_of_log_handlers} handlers")

    root_logger.info("First Statement from Initialize Logger.")

    return root_logger


def _ensure_setting_log_output_is_valid(log_output: str) -> None:

    valid_values = {"CONSOLE", "FILE", "ALL"}

    if log_output not in valid_values:
        error_text = (
            f"Value of env var: LOG_OUTPUT was set as: {log_output} - this is invalid."
        )
        raise Exception(error_text)


def _create_timed_rotating_file_handler() -> TimedRotatingFileHandler:

    print("Creating TimedRotatingFileHandler from log settings...")
    rotate_when = os.getenv("LOG_ROTATE_WHEN", "midnight")
    log_rotate_interval = os.getenv("LOG_ROTATE_INTERVAL", "1")
    rotate_interval = int(log_rotate_interval)
    path_to_logfile = _get_path_to_create_logs()
    log_files_limit = int(os.getenv("LOG_FILES_LIMIT", "2"))
    return TimedRotatingFileHandler(
        filename=path_to_logfile,
        when=rotate_when,
        interval=rotate_interval,
        backupCount=log_files_limit,
        utc=True,
    )


def _create_stream_handler() -> logging.StreamHandler:

    log_console_stream = os.getenv("LOG_CONSOLE_STREAM", "STDOUT")

    if log_console_stream == "STDOUT":
        stream = sys.stdout
    elif log_console_stream == "STDERR":
        stream = sys.stdout
    else:
        log_console_stream = "STDOUT"
        stream = sys.stdout

    print(f"Creating StreamHandler for stream: {log_console_stream}...")

    return logging.StreamHandler(stream=stream)


def _get_log_handlers() -> set:

    log_output = os.getenv("LOG_OUTPUT", "CONSOLE")

    _ensure_setting_log_output_is_valid(log_output)

    if log_output == "CONSOLE":
        return {_create_stream_handler()}
    elif log_output == "FILE":
        return {_create_timed_rotating_file_handler()}
    elif log_output == "ALL":
        stream_handler = logging.StreamHandler(stream=sys.stdout)
        trf_handler = _create_timed_rotating_file_handler()

        return {stream_handler, trf_handler}


def _get_path_to_create_logs() -> str:

    logs_dir_path_template = os.getenv("LOG_DIRECTORY_TEMPLATE", "./logs")
    root_dir = settings.PRODUCT_ROOT_DIR
    logs_dir_path = logs_dir_path_template.replace(".", root_dir)
    print("Desired path to logs directory is:")
    print(logs_dir_path)
    # print(pformat(logs_dir_path))

    if not os.path.isdir(logs_dir_path):
        print("Logs directory does not exist.")
        os.makedirs(logs_dir_path, exist_ok=True)
        print("Logs directory created.")

    desired_filename = os.getenv("LOG_FILE_NAME", "scalerts.log")

    path_to_logfile = f"{logs_dir_path}/{desired_filename}"
    print(f'Path to Logfile is: "{path_to_logfile}"')

    return path_to_logfile


def _get_log_level_from_settings() -> int:

    log_level = os.getenv("LOG_LEVEL", "DEBUG")
    print(f'Value of "LOG_LEVEL" is: {log_level}')
    level_str = log_level.upper()

    if level_str == "DEBUG":
        log_level = logging.DEBUG
    elif level_str == "INFO":
        log_level = logging.INFO
    elif level_str == "WARNING":
        log_level = logging.WARNING
    elif level_str == "ERROR":
        log_level = logging.ERROR
    else:
        log_level = logging.WARNING

    return log_level


def _set_level_and_format_in_log_handler(
    log_handler, log_fmt: logging.Formatter, log_level: int
):

    log_handler.setLevel(log_level)
    log_handler.setFormatter(log_fmt)

    return log_handler
