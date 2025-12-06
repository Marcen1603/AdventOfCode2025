class IdValidator:

    def __init__(self, id_string: str):

        self.invalid_ids = []
        self.id_string_array = id_string.split(",")
        self.id_tuples = []

    def convert_string_to_int(self) -> (int, int):

        # Input format: 95-115
        for id in self.id_string_array:
            id_range_split = id.split("-")
            try:
                lower_id_range = int(id_range_split[0])
                upper_id_range = int(id_range_split[1])
                self.id_tuples.append((lower_id_range, upper_id_range))
            except ValueError:
                print(f"Not abel to convert strings (lower: {id_range_split[0]}, upper: {id_range_split[1]}) to int")

    def filter_patterns_twice(self):

        for id_tuple in self.id_tuples:
            if id_tuple is None:
                raise ValueError("Id tuple is not set!")

            # Iterate threw id range
            for id in range(id_tuple[0], id_tuple[1] + 1):

                # Convert int back to string for a better pattern check
                string_value = str(id)
                print(f"Check id: {string_value}")

                # Check if pattern can exist twice
                if len(string_value) % 2 == 0:

                    # Get first half of the string
                    first_string_part = ""
                    for string_iterator in range(int(len(string_value) / 2)):
                        first_string_part += string_value[string_iterator]

                    # Get second half of the string
                    second_string_part = ""
                    for string_iterator in range(int(len(string_value) / 2), len(string_value)):
                        second_string_part += string_value[string_iterator]

                    if first_string_part == second_string_part:
                        self.invalid_ids.append(id)


    def filter_patterns_multiple_times(self):

        for id_tuple in self.id_tuples:
            if id_tuple is None:
                raise ValueError("Id tuple is not set!")

            # Iterate threw id range
            for x in range(id_tuple[0], id_tuple[1] + 1):

                # Convert int back to string for a better pattern check
                string_value = str(x)
                print(f"Check id: {string_value}")

                # Create substring from 1 upto length of the string_value and check for patterns
                check = False
                for y in range(len(string_value)):

                    substring = ""
                    for pattern_check in range(y + 1):
                        substring += string_value[pattern_check]

                    # Check if substring can appear multiple times without rest
                    valid_pattern_positions = (len(string_value) % len(substring)) == 0 and len(substring) <= int(len(string_value) / 2)
                    if valid_pattern_positions:

                        # Check each pattern step exp. for 65656565 with 65 than there are 4 checks 65|65|65|65
                        pattern_checks = int(len(string_value) / len(substring))
                        print(f"Check {substring} for {pattern_checks} equal occurs")

                        times_occur = 0
                        for pattern_check in range(pattern_checks):

                            # Get part of string_value
                            pattern_check_string = ""
                            for elem in range(len(substring)):
                                pattern_check_string += string_value[elem + (pattern_check * len(substring))]

                            print(f"Check if the {str(pattern_check)} part of the string_value ({pattern_check_string}) is "
                                  f"equal to substring")

                            if pattern_check_string == substring:
                                times_occur += 1
                            else:
                                break

                        if times_occur == pattern_checks:
                            check = True
                            break

                    else:

                        print(f"Pattern {substring} is not valid for a check")

                if check:
                    self.invalid_ids.append(string_value)


    def run(self, multiple: bool):

        self.convert_string_to_int()
        if multiple:
            self.filter_patterns_multiple_times()
        else:
            self.filter_patterns_twice()
        print(f"Invalid ids: {self.invalid_ids}")