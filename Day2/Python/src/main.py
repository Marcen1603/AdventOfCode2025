from Day2.Python.src.IdValidator import IdValidator

if __name__ == "__main__":
    id_string = ("9226466333-9226692707,55432-96230,4151-6365,686836-836582,519296-634281,355894-471980,971626-1037744,"
                 "25107-44804,15139904-15163735,155452-255998,2093-4136,829776608-829880425,4444385616-4444502989,"
                 "2208288-2231858,261-399,66-119,91876508-91956018,2828255673-2828317078,312330-341840,6464-10967,"
                 "5489467-5621638,1-18,426-834,3434321102-3434378477,4865070-4972019,54475091-54592515,147-257,"
                 "48664376-48836792,45-61,1183-1877,24-43")

    result_twice = 0
    id_validator = IdValidator(id_string)
    id_validator.run(False)

    for y in id_validator.invalid_ids:
        result_twice += int(y)

    result_multiple = 0
    id_validator = IdValidator(id_string)
    id_validator.run(True)

    for y in id_validator.invalid_ids:
        result_multiple += int(y)

    print(f"Sum up for twice occur: {result_twice}")
    print(f"Sum up for multiple occur: {result_multiple}")
