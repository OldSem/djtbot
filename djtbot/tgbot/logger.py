import logging
import sys

logger_djtbot = logging.getLogger('Django')
formatter = logging.Formatter(
    '%(asctime)s (%(filename)s:%(lineno)d %(threadName)s) %(levelname)s - %(name)s: "%(message)s"'
)

console_output_handler = logging.StreamHandler(sys.stderr)
console_output_handler.setFormatter(formatter)
logger_djtbot.addHandler(console_output_handler)

logger_djtbot.setLevel(logging.ERROR)