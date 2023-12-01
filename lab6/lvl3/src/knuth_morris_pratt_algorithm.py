def knuth_morris_prat(haystack: str, needle: str) -> list[int]:
    """
    Search for occurrences of the given pattern in the input text using the Knuth-Morris-Pratt algorithm.

    :param haystack: The text in which we search for occurrences.
    :param needle: The pattern we are searching for.
    :return: A list containing the starting indices of all occurrences of the pattern in the text.
    """
    prefix = build_prefix_table(needle)
    needle_index = 0
    haystack_index = 0
    result = []
    while haystack_index < len(haystack):
        if needle[needle_index] == haystack[haystack_index]:
            haystack_index += 1
            needle_index += 1
            if needle_index == len(needle):
                result.append(haystack_index - needle_index)
                needle_index = prefix[needle_index - 1]
        elif mismatch_and_not_zero(needle, needle_index, haystack, haystack_index):
            needle_index = prefix[needle_index - 1]
        else:
            haystack_index += 1
    return result


def build_prefix_table(pattern: str) -> list[int]:
    """
    Funk to build prefix table for patter
    :param pattern: The pattern for which the prefix table is built.
    :return: A list representing the prefix table.
    """
    prefix = [0] * len(pattern)
    start = 0
    end = 1
    while end < len(pattern):
        if pattern[end] != pattern[start] and start == 0:
            prefix[end] = 0
            end += 1
        if pattern[end] != pattern[start] and start != 0:
            start = prefix[start - 1]
        if pattern[end] == pattern[start]:
            prefix[end] = start + 1
            end += 1
            start += 1
    return prefix


def mismatch_and_not_zero(
    needle: str, needle_index: int, haystack: str, haystack_index: int
) -> bool:
    return needle[needle_index] != haystack[haystack_index] and needle_index != 0
