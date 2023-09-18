#!/usr/bin/env python3
import os
import shutil

mapping = {
    "bolt": "bolt",
    "crosshairs": "crosshairs",
    "curve": "curve",
    "default": "default",
    "ex": "ex",
    "eye": "eye",
    "fox": "fox",
    "frame": "frame",
    "hole": "hole",
    "play": "play",
    "wing": "wing",
}

if __name__ == "__main__":
    if os.path.exists("hats"):
        shutil.rmtree("hats")
    os.makedirs("hats")
    for spoken, source in mapping.items():
        os.symlink(
            os.path.join("..", "source", "{}.svg".format(source)),
            os.path.join(".", "hats", "{}.svg".format(source)),
        )
