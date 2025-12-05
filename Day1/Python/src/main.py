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
    result = 0
    safe = Safe()
    for instruction in instructions:
        safe.rotating(instruction[0], instruction[1])
        if safe.dial == 0:
            result += 1

    # Show result
    print(f"Result: {result}")
