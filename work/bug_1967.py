try:
    match ():
        case b'':
            pass
except* {}:
    pass
else:
    name_1

# output:
# python: Python/flowgraph.c:511: no_redundant_jumps: Assertion `0' failed.
