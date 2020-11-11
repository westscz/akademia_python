import re
from timeit import timeit


def abr(words):
    filtered = re.findall(r'[A-Z]+\'?[A-Z]?', words.upper())
    acronym = ''.join([chr[0] for chr in filtered])
    return acronym

def abrs(text):
    return "".join([x[0] for x in text.replace('_'," ").split() if x])


text = 'The Road _Not_ Taken'
print(text)

print(
    'regex',
    timeit(
        "abr(text)",
        f"from __main__ import abr; text='{text}'"
    )
)

print(
    'join split',
    timeit(
        "abrs(text)",
        f"from __main__ import abrs; text='{text}'"
    )
)



# print timeit("abrs(text)", "from __main__ import re_find; string='lookforme'; text='look'")