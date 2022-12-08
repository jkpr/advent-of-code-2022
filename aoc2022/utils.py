import json
import logging


def setup_logging():
    parent = __name__[: __name__.rfind(".")]
    logger = logging.getLogger(parent)
    logger.setLevel(logging.DEBUG)
    formatter = logging.Formatter(
        fmt="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )
    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(logging.NOTSET)
    stream_handler.setFormatter(formatter)
    logger.addHandler(stream_handler)


def print_json(obj, **kwargs):
    print(json.dumps(obj, sort_keys=True, indent=2, default=repr))
