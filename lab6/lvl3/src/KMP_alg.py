def kmp(haystack, needle):
    pi = find_pi(needle)
    needle_index = 0
    haystack_index = 0
    result = []
    while haystack_index < len(haystack):
        if needle[needle_index] == haystack[haystack_index]:
            haystack_index += 1
            needle_index += 1
        if needle_index == len(needle):
            result.append(haystack_index - needle_index)
            needle_index = pi[needle_index - 1]
        elif (
            haystack_index < len(haystack)
            and needle[needle_index] != haystack[haystack_index]
        ):
            if needle_index != 0:
                needle_index = pi[needle_index - 1]
            else:
                haystack_index += 1
    return result


def find_pi(pattern):
    pi = [0] * len(pattern)
    start = 0
    end = 1
    while end < len(pattern):
        if pattern[end] != pattern[start] and start == 0:
            pi[end] = 0
            end += 1
        if pattern[end] != pattern[start] and start != 0:
            start = pi[start - 1]
        if pattern[end] == pattern[start]:
            pi[end] = start + 1
            end += 1
            start += 1
    return pi
