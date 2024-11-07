import argparse
import math
import turtle

# Parse command-line argument for file path
parser = argparse.ArgumentParser()
parser.add_argument('file_PATH', type=str)
file_PATH = parser.parse_args()
content = file_PATH.file_PATH

# Set up Turtle screen and turtle object
display = turtle.Screen()
display.bgcolor('olive')
scirroco = turtle.Turtle()
scirroco.pensize(9)
scirroco.shape('turtle')
scirroco.color('white')


def print_commands(x_cord, y_cord, direction, instruction, instructions_count):
    action = instruction[0]
    if action == 'move':
        action_gerund = 'moving'
    elif action == 'turn':
        action_gerund = 'turning'
    else:
        action_gerund = action

    instruction_gerund = [action_gerund] + instruction[1:]
    
    if len(instruction) <= 4:
        print(" ".join(instruction_gerund).capitalize(), f'(instruction {instructions_count})')
        print(f'Im at {(x_cord, y_cord)} facing {direction} degrees')
    else:
        print(f"I've encountered an instruction I don't understand, aborting (instruction {instructions_count})")


def simulate_rover(path):
    # Read instructions from file
    with open(path, 'r') as f:
        instructions = f.readlines()

    x_cord = 0
    y_cord = 0
    direction = 0
    instructions_count = 0
    print(f'Im at {(x_cord, y_cord)} facing {direction} degrees')

    for instruction in instructions:
        instructions_count += 1
        instruction = instruction.lower().strip().split()

        # Skip empty instructions
        if not instruction:
            continue

        if len(instruction) <= 4:
            if 'move' in instruction:
                # Process move instructions
                values = instruction
                if values[1].isdigit():
                    displacement = int(values[1])

                    if 'forward' == instruction[-1]:
                        y_cord += int((displacement * math.cos(math.radians(direction))))
                        x_cord += int((displacement * math.sin(math.radians(direction))))

                    elif 'backward' == instruction[-1]:
                        x_cord -= int((displacement * math.sin(math.radians(direction))))
                        y_cord -= int((displacement * math.cos(math.radians(direction))))

                    scirroco.goto(x_cord * 10, y_cord * 10)
                    scirroco.setheading(direction)

            elif 'turn' in instruction:
                # Process turn instructions
                if 'clockwise' == instruction[-1]:
                    direction += int(instruction[1])
                elif 'counterclockwise' == instruction[-1]:
                    direction -= int(instruction[1])
        else:
            print(f"I've encountered an instruction I don't understand, aborting (instruction {instructions_count})")
            break

        print_commands(x_cord, y_cord, direction, instruction, instructions_count)

    display.exitonclick()


# Start simulation
simulate_rover(content)
# turtle.mainloop()
