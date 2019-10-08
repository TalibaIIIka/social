import argparse
import pathlib

from trafaret_config import commandline

from app_soc.utils import CONFIG_TRAFARET


BASE_DIR = pathlib.Path(__file__).parent.parent
DEFAULT_CONFIG_PATH = BASE_DIR / 'config' / 'config.yml'


def get_config(argv=None):
    ap = argparse.ArgumentParser()
    commandline.standard_argparse_options(
        ap,
        default_config=DEFAULT_CONFIG_PATH
    )

    options, __ = ap.parse_known_args(argv)

    config = commandline.config_from_options(options, CONFIG_TRAFARET)
    return config
