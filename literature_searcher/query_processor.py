database = {
    "shakespeare": """William Shakespeare (26 April 1564 - 23 April 1616) was an
        English poet, playwright, and actor, widely regarded as the
        greatest writer in the English language and the world's
        pre-eminent dramatist.""",
    "asimov": """Isaac Asimov (2 January 1920 - 6 April 1992) was an
        American writer and professor of Biochemistry, famous for
        his works of hard science fiction and popular science.""",
    "orwell": """Eric Arthur Blair (25 June 1903 – 21 January 1950), better known by his pen name George Orwell, was an English novelist, essayist, journalist, and     critic. His work is characterised by lucid prose, social criticism, opposition to totalitarianism, and support of democratic socialism""",
    "lee": """Nelle Harper Lee (April 28, 1926 – February 19, 2016) was an American novelist. She penned the 1960 novel To Kill a Mockingbird that won the 1961 Pulitzer Prize and became a classic of modern American literature."""
}


def process(query):
    return [val for key, val in database.items() if key in query.lower()]
