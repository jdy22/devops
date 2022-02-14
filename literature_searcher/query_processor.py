database = {
    "shakespeare": """William Shakespeare (26 April 1564 - 23 April 1616) was an
        English poet, playwright, and actor, widely regarded as the
        greatest writer in the English language and the world's
        pre-eminent dramatist.""",
    "asimov": """Isaac Asimov (2 January 1920 - 6 April 1992) was an
        American writer and professor of Biochemistry, famous for
        his works of hard science fiction and popular science.""",
}


def process(query):
    return [val for key, val in database.items() if key in query.lower()]
