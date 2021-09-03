def writers(writer):
    if writer:
        return writer.strip()
    else:
        return None


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
