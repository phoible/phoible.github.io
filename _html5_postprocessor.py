import sys

sentinels = ('AUTO-REMOVED DUMMY', 'auto-removed-dummy')

depth = 0
for line in sys.stdin:
    # only write lines that don't have our sentinel values
    keep = True
    for sentinel in sentinels:
        if sentinel in line:
            keep = False
            break
    # the depth check is hackish, it relies on the prior knowledge that we're
    # only putting in one top-level dummy heading (it won't handle mid-level
    # dummies)
    if '<section' in line:
        depth += 1
    elif '</section' in line:
        depth -= 1
    if keep and depth > 0:
        sys.stdout.write(line)
