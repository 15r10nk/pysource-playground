try:
    match name_2:
        case (0):
            pass
except* '':
    pass
finally:
    name_0

# output:
# python: Python/flowgraph.c:511: no_redundant_jumps: Assertion `0' failed.
