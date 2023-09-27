#!/usr/bin/env python3
import os
import shutil

mapping = {
    "bolt": "gate",
    "crosshairs": "fang",
    "curve": "knight",
    "default": "default",
    "ex": "rook",
    "eye": "church",
    "fox": "shroom",
    "frame": "horn",
    "hole": "wrench",
    "play": "play",
    "wing": "gem",
}

if __name__ == "__main__":
    if os.path.exists("hats"):
        shutil.rmtree("hats")
    os.makedirs("hats")
    for spoken, source in mapping.items():
        os.symlink(
            os.path.join("..", "source", "{}.svg".format(source)),
            os.path.join(".", "hats", "{}.svg".format(spoken)),
        )
