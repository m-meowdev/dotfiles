from os import path
import json

colorscheme = ["catppuccin", "mocha"]
colors = {}
colorscheme_file = path.join(path.expanduser("~"), ".config", "qtile", "colorschemes", f"{colorscheme[0]}.json")

if not path.isfile(colorscheme_file):
    raise Exception(f"'{colorscheme_file}' does not exist!")

colors = json.load(open(colorscheme_file))[colorscheme[1]]
