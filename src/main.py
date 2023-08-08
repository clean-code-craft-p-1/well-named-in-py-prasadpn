from test.test_wire_color_pair import test_number_to_pair, test_pair_to_number
from test.test_print_color_code import test_print_output


if __name__ == '__main__':
    test_number_to_pair(4, 'White', 'Brown')
    test_number_to_pair(5, 'White', 'Slate')
    test_pair_to_number('Black', 'Orange', 12)
    test_pair_to_number('Violet', 'Slate', 25)
    test_pair_to_number('Red', 'Orange', 7)
    print_output = test_print_output()
    print_output.test_print_output_with_header(25)
    print('Done :)')
