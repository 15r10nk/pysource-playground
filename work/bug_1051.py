try:
    match name_5:
        case b'':
            pass
except* name_5:
    pass
finally:
    name_5

# output:
# python: Python/flowgraph.c:511: no_redundant_jumps: Assertion `0' failed.
