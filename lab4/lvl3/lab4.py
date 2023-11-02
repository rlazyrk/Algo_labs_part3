def read_from_file(file_name: str):
    with open(file_name, "r") as file:
        n = int(file.readline().strip())
        print(n)
        start = tuple(map(int, file.readline().strip().split(',')))
        print(start)
        destination = tuple(map(int, file.readline().strip().split(',')))
        print(destination)
    return n, start, destination


def find_min_knight_path(board_side: int, start: tuple, destination: tuple):
    row = [2, 2, -2, -2, 1, 1, -1, -1]
    col = [-1, 1, 1, -1, 2, -2, 2, -2]
    counter = 0
    queue = [(start, counter)]
    visited = set()
    while queue:
        (x, y), counter = queue.pop(0)
        visited.add((x, y))

        if (x, y) == destination:
            return counter
        for i in range(len(row)):
            k = x + row[i]
            l = y + col[i]
            if k < board_side and l < board_side and (k, l) not in visited and k >= 0 and l >= 0:
                queue.append(((k, l), counter + 1))
                visited.add((k, l))


def write_to_file(number: int)-> None:
    with open("output.txt","w") as file:
        file.write(str(number))

n, start, end = read_from_file('input.txt')
print(find_min_knight_path(n, start, end))
write_to_file(find_min_knight_path(n, start, end))