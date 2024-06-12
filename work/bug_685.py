try:
    match {}:
        case '':
            pass
except* name_4:
    pass
else:
    b''

# output:
# python: Python/flowgraph.c:511: no_redundant_jumps: Assertion `0' failed.
