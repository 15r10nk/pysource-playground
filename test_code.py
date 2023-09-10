import sys
import pathlib

source=pathlib.Path(sys.argv[1]).read_text()

compile(source,"<file>","exec")
