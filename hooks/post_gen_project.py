#!/usr/bin/env python

import os
import sys
from pathlib import Path

module_name = '{{ cookiecutter.model_type }}'

PROJECT_DIRECTORY = Path(os.path.realpath(os.path.curdir))


FILES = {"zeuthen": PROJECT_DIRECTORY / Path("zeuthen-csrtrk.in"),
         "bc": PROJECT_DIRECTORY / Path("bc-csrtrk.in")}

TARGET = PROJECT_DIRECTORY / "csrtrk.in"

if __name__ == '__main__':
    if '{{ cookiecutter.model_type == "zeuthen" }}':
        FILES["bc"].unlink()
        FILES["zeuthen"].rename(TARGET)

    elif '{{ cookiecutter.model_type == "bc" }}':
        FILES["zeuthen"].unlink()
        FILES["bc"].rename(TARGET)
    else:
        sys.exit(1)

    (Path(PROJECT_DIRECTORY) / "in").mkdir()
    (Path(PROJECT_DIRECTORY) / "out").mkdir()
