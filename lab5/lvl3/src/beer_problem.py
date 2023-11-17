def read_data_from_file(filename: str) -> tuple:
    """
    Func to reading form file
    :param filename: input file in .txt format
    :return: tuple with num of people, num of beer types and list of beer preferences in format ["srt", "str" ...]
    """
    with open(filename, "r") as file:
        num_people, num_beer_types = map(int, file.readline().split())
        beer_preferences = file.readline().split()
    return num_people, num_beer_types, beer_preferences


def create_matrix(num_people: int, num_beer_types: int, beer_preferences: list) -> list:
    """
    Func to create matrix of dependencies for beer_preferences and people
    :param num_people:
    :param num_beer_types:
    :param beer_preferences:
    :return: list where rows is types of beer and columns is people
    """
    beer_matrix = [[0] * num_people for _ in range(num_beer_types)]
    for person_index in range(num_people):
        for beer_index in range(num_beer_types):
            if beer_preferences[person_index][beer_index] == "Y":
                beer_matrix[beer_index][person_index] = 1
    return beer_matrix


def beer_combinations(num_people: int, num_beer_types: int, beer_matrix: list) -> list:
    """
    Func to find all possible combination of beers to satisfies all people
    :param num_people:
    :param num_beer_types:
    :param beer_matrix:
    :return: list with beers combination
    """

    def satisfies_all(possible_combination: list) -> bool:
        """
        Helpful func to check that combination satisfies all people
        :param possible_combination:
        :return: True of False
        """
        for person_index in range(num_people):
            if (
                sum(
                    beer_matrix[beer_type][person_index]
                    for beer_type in possible_combination
                )
                < 1
            ):
                return False
        return True

    def generate_combinations(start_index: int, current_combination: list):
        """
        Func to generate all possible combination of beer types
        :param start_index:
        :param current_combination:
        :return: return nothing because it modifies input list
        """
        if satisfies_all(current_combination):
            possible_combinations.append(list(current_combination))
        for i in range(start_index, num_beer_types):
            current_combination.append(i)
            generate_combinations(i + 1, current_combination)
            current_combination.pop()

    possible_combinations = []
    generate_combinations(0, [])
    print(possible_combinations)
    return possible_combinations


def write_to_file(answer: int, file_mame: str) -> None:
    """
    Funk to write answer in to file
    :param answer:
    :param file_mame:
    :return:
    """
    with open(file_mame, "w") as file:
        file.write(str(answer))


def beer_problem_answer(
    num_people: int, num_beer_types: int, beer_preferences: list
) -> int:
    """
    Func solution of beer problem
    :param num_people:
    :param num_beer_types:
    :param beer_preferences:
    :return: number of min beer types that have to buyed
    """
    answer = float("inf")
    for combination in beer_combinations(
        num_people,
        num_beer_types,
        create_matrix(num_people, num_beer_types, beer_preferences),
    ):
        if answer > len(combination):
            answer = len(combination)
    return answer
