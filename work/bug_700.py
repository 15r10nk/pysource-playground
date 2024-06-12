try:
    match '':
        case 0:
            pass
except* name_1:
    pass
finally:
    ()

# output:
# python: Python/flowgraph.c:511: no_redundant_jumps: Assertion `0' failed.
