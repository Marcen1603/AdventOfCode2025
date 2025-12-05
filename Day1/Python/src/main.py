from Day1.Python.src.Save import Direction, Safe

if __name__ == "__main__":

    # Load instructions
    path_to_instructions = "instructions.txt"
    instructions = []
    with open(path_to_instructions) as f:

        # Get movement and direction
        for line in f.readlines():
            direction = line[0]
            movement = ''
            for char in range(1, len(line)):
                movement += line[char]

            instructions.append((Direction.from_str(direction), int(movement)))

    # Execute instructions
    step_over_zero = 0
    end_result_zero = 0
    safe = Safe()
    for instruction in instructions:
        step_over_zero += safe.rotating(instruction[0], instruction[1])
        if safe.dial == 0:
            end_result_zero += 1

    # Show result
    print(f"Step over zero: {step_over_zero}")
    print(f"End result zero: {end_result_zero}")
    print(f"Total: {step_over_zero + end_result_zero}")
