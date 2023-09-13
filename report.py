import pathlib

for f in (pathlib.Path()/"work").glob("bug*.py"):
    text=f.read_text()
    if "SystemError" in text:
        print()
        print("``` python")
        print(f.read_text())
        print("```")
