import sys
import pathlib

source=pathlib.Path(sys.argv[1]).read_text()

compile(source,sys.argv[1],"exec")
