def knuth_morris_prat(haystack, needle):
    prefix = build_prefix(needle)
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
        elif check_miss_math_needle_not_zero(needle, needle_index, haystack, haystack_index):
            needle_index = prefix[needle_index - 1]
        else:
            haystack_index += 1
    return result


def build_prefix(pattern):
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


def check_miss_math_needle_not_zero(needle, needle_index, haystack, haystack_index):
    return needle[needle_index] != haystack[haystack_index] and needle_index != 0
