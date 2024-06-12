try:
    match name_4:
        case b'':
            pass
except* name_4:
    pass
finally:
    name_1

# output:
# python: Python/flowgraph.c:511: no_redundant_jumps: Assertion `0' failed.
