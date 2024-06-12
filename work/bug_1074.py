try:
    pass
except* name_3:
    pass
finally:
    match name_3:
        case True:
            pass
{()}

# output:
# python: Python/flowgraph.c:511: no_redundant_jumps: Assertion `0' failed.
