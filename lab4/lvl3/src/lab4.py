def read_from_file(file_name: str) -> tuple:
    """
    :param file_name:
    :return: tuple with board_side, start point, destination point
    """
    with open(file_name, "r") as file:
        board_side = int(file.readline().strip())
        start = tuple(map(int, file.readline().strip().split(",")))
        destination = tuple(map(int, file.readline().strip().split(",")))
    return board_side, start, destination


def find_min_knight_path(board_side: int, start: tuple, destination: tuple) -> int:
    """
    :param board_side:
    :param start:
    :param destination:
    :return: lenght of knight`s path from one point to another
    """
    row = [2, 2, -2, -2, 1, 1, -1, -1]
    col = [-1, 1, 1, -1, 2, -2, 2, -2]
    counter = 0
    queue = [(start, counter)]
    visited = set()
    while queue:
        current_position, counter = queue.pop(0)
        x, y = current_position
        visited.add(current_position)

        if current_position == destination:
            return counter
        for i in range(len(row)):
            new_x = x + row[i]
            new_y = y + col[i]
            if (
                new_x < board_side
                and new_y < board_side
                and (new_x, new_y) not in visited
                and new_x >= 0
                and new_y >= 0
            ):
                queue.append(((new_x, new_y), counter + 1))
                visited.add((new_x, new_y))


def write_to_file(number: int, file_name: str) -> None:
    """
    :param number:
    write number to file.txt
    """
    with open(file_name, "w") as file:
        file.write(str(number))


if __name__ == "__main__":
    n, start, end = read_from_file("input.txt")
    print(find_min_knight_path(n, start, end))
    write_to_file(find_min_knight_path(n, start, end), "output.txt")

