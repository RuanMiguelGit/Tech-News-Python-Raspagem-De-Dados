def writers(possibilities):

    if possibilities[0]:
        writer = possibilities[0].strip()
    elif possibilities[1]:
        writer = possibilities[1].strip()
    else:
        writer = "Equipe TecMundo"
    return writer


def comments(comments_count):
    if comments_count is not None and len(comments_count) > 0:
        return int(comments_count)
    else:
        return


def shares(shares_count):
    if shares_count is not None and len(shares_count) > 0:
        return int(shares_count.split()[0])
    else:
        return 0
