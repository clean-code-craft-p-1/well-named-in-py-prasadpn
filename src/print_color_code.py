from wire_color_pair import get_color_from_pair_number
from tabulate import tabulate


def print_wire_color_code(pair_number):
    pair_value = get_color_from_pair_number(pair_number)
    table_output = tabulate([[pair_number, pair_value[0], pair_value[1]]],
                            headers=['Pair Number', 'Major', 'Minor'],
                            tablefmt='orgtbl')
    return table_output
