# Purpose

This tool lets you easily manage which hat is mapped to which svg file by creating a directory of symlinks to your svg files.
This allows you to for instance pick and choose hats from different hat collections without having to manually copy svg files around from different directories.

# Usage

* Add the hats you want to use into the `source` directory, separating different hat collections into different directories if you so wish.

* Edit the `mapping` variable in the `create_links.py` script to change which hat is mapped to which svg file.

* Run `./create_links.py`

* Set up cursorless to read its svgs from the `hats` directory which is created in the same directory as this file.