import argparse
import math
import turtle

parser = argparse.ArgumentParser()
parser.add_argument('file_PATH', type=str)
file_PATH = parser.parse_args().file_PATH

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
        if action == 'move':
            print(f"{action_gerund.capitalize()} {float(instruction[1]):.2f} meters {instruction[-1]} (instruction {instructions_count:.2f})")
        elif action == 'turn':
            print(f"{action_gerund.capitalize()} {int(instruction[1]):.2f} degrees {instruction[-1]} (instruction {instructions_count:.2f})")
        print(f"I'm at ({(x_cord):.2f}, {(y_cord):.2f}) facing {direction:.2f} degrees")
    else:
        print(f"I've encountered an instruction I don't understand, aborting (instruction {instructions_count:.2f})")

        
def simulate_rover(path):
    try:
        with open(path, 'r') as f:
            instructions = f.readlines()
    except FileNotFoundError:
        print("File not found. Please provide a valid file path.")
        return

    x_cord = 0.0
    y_cord = 0.0
    direction = 0.0
    instructions_count = 0
    print(f"I'm at ({x_cord:.2f}, {y_cord:.2f}) facing {direction:.2f} degrees")

    for instruction in instructions:
        instructions_count += 1
        instruction = instruction.lower().strip().split()

        if not instruction:
            continue

        if len(instruction) <= 4:
            if 'move' in instruction:
                try:
                    displacement = float(instruction[1])
                except (ValueError, IndexError):
                    print(f"Invalid displacement value in instruction {instructions_count:.2f}")
                    break

                if 'forward' == instruction[-1]:
                    y_cord += displacement * math.cos(math.radians(direction))
                    x_cord += displacement * math.sin(math.radians(direction))
                elif 'backward' == instruction[-1]:
                    y_cord -= displacement * math.cos(math.radians(direction))
                    x_cord -= displacement * math.sin(math.radians(direction))

            elif 'turn' in instruction:
                try:
                    angle = int(instruction[1])
                except (ValueError, IndexError):
                    print(f"Invalid angle value in instruction {instructions_count:.2f}")
                    break

                if 'clockwise' == instruction[-1]:
                    direction += angle
                elif 'counterclockwise' == instruction[-1]:
                    direction -= angle
                direction = direction % 360
                
                scirroco.goto(x_cord * 10, y_cord * 10)
                scirroco.setheading(direction)
        else:
            print(f"I've encountered an instruction I don't understand, aborting (instruction {instructions_count:.2f})")
            break

        print_commands(x_cord, y_cord, direction, instruction, instructions_count)
    display.exitonclick()        
simulate_rover(file_PATH)