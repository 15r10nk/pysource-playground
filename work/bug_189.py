try:
    match something:
        case 0:
            pass
except* {}:
    pass
else:
    something

# output:
# python: Python/flowgraph.c:511: no_redundant_jumps: Assertion `0' failed.
