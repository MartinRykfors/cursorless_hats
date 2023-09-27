#!/usr/bin/env python3
import os
import shutil

mapping = {
    "bolt": "source/gate.svg",
    "crosshairs": "source/fang.svg",
    "curve": "source/knight.svg",
    "default": "source/default.svg",
    "ex": "source/rook.svg",
    "eye": "source/church.svg",
    "fox": "source/shroom.svg",
    "frame": "source/horn.svg",
    "hole": "source/wrench.svg",
    "play": "source/play.svg",
    "wing": "source/gem.svg",
}

if __name__ == "__main__":
    root = os.path.dirname(os.path.abspath(__file__))
    output_dir = os.path.join(root, "hats")

    if os.path.exists(output_dir):
        shutil.rmtree(output_dir)
    os.makedirs(output_dir)

    for spoken, source in mapping.items():
        src = os.path.relpath(os.path.join(root, source), output_dir)
        dst = os.path.join(output_dir, "{}.svg".format(spoken))
        print("Linking {} -> {}".format(dst, src))
        os.symlink(src, dst)
