try:
    match name_5:
        case '':
            pass
except* False:
    pass
finally:
    name_4

# output:
# python: Python/flowgraph.c:511: no_redundant_jumps: Assertion `0' failed.
