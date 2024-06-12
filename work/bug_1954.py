try:
    match name_2:
        case '':
            pass
except* name_4:
    pass
finally:
    name_4

# output:
# python: Python/flowgraph.c:511: no_redundant_jumps: Assertion `0' failed.
