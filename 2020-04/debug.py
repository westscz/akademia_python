"""
Article:
"""


def lower_camel_case(string: str) -> str:
    words = string.split(" ")
    title_words = [w.title() for w in words]
    new_string = "".join(title_words)
    return new_string


breakpoint()
result = lower_camel_case("simple function name")
assert result == "simpleFunctionName"
