from Day2.Python.src.IdValidator import IdValidator


def test_id_validator_twice():

    id_string = ("11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,"
                 "38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124")

    result = 0
    id_validator = IdValidator(id_string)
    id_validator.run(False)

    for y in id_validator.invalid_ids:
        result += y

    assert result == 1227775554


def test_id_validator_multiple():

    id_string = ("11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,"
                 "38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124")

    id_validator = IdValidator(id_string)
    id_validator.run(True)

    result = 0
    for y in id_validator.invalid_ids:
        result += int(y)

    assert result == 4174379265