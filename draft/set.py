print(set([1, 2, 3, 4, 5, 6, 7, 5, 5, 5, 4, 3, 2, 1]))
print(set(["a", "b", "c", "c", "d", "a", "a"]))
print(set([True, True, True, True, False, None]))
print(set([(1, 2), (2, 3), (3, 2), (1, 2)]))

"> {1, 2, 3, 4, 5, 6, 7}"
"> {'d', 'c', 'b', 'a'}"
"> {False, True, None}"
"> {(2, 3), (3, 2), (1, 2)}"

set([[1], [2], [3]])
"> TypeError: unhashable type: 'list'"
