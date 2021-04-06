# -*- coding: utf-8 -*-
# fmt: off

import pathlib


__version__ = '1.0'


# always look relative from the project's root directory
_root_path = pathlib.Path(__file__).parent.parent
_DATA_DIR = 'data'


# fmt: off
class ENV:

    ROOT_DIR:    pathlib.Path = _root_path
    SRC_DIR:     pathlib.Path = _root_path / 'irt'
    CONF_DIR:    pathlib.Path = _root_path / 'conf'
    DATA_DIR:    pathlib.Path = _root_path / _DATA_DIR
    DATASET_DIR: pathlib.Path = _root_path / _DATA_DIR / 'irt'
# fmt: on


class IRTError(Exception):
    def __init__(self, msg: str):
        super().__init__(msg)