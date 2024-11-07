Here’s the updated `README.md` file to reflect the new code features, including command-line argument parsing and Turtle graphics.

---

# Mars Rover Simulation

## Description
This project simulates a Mars rover’s movement on a 2D plane using Python's Turtle graphics to visualize its path. The rover starts from an initial position and orientation, updating its coordinates and direction based on movement and rotation commands. The real-time output and graphical path tracing make this a helpful tool for understanding basic robotics and simulation.

## Background
We simulate the Mars rover on an infinite, two-dimensional plane. The rover's position is represented by coordinates \((x, y)\), and its orientation is given by an angle in degrees:
- **0°** is due **north**.
- **90°** is due **east**.
- **180°** is due **south**.
- **270°** is due **west**.

The rover begins at position \((0, 0)\) and faces north \((0°)\). Commands control its movements and turns, allowing it to navigate the simulated Martian surface.

## Features
- **Graphical Visualization**: Turtle graphics display the rover's path on the screen.
- **Command-Line Argument**: Users can specify a path to the instruction file directly from the command line.
- **Instruction Feedback**: The program provides real-time position and orientation updates after each command.

## Command List Format
Commands are read from a text file, with each command on a new line:

1. **Move Command**:
   - `move forward X` - Moves the rover forward by \(X\) meters.
   - `move backward X` - Moves the rover backward by \(X\) meters.

2. **Turn Command**:
   - `turn clockwise X` - Turns the rover clockwise by \(X\) degrees.
   - `turn counterclockwise X` - Turns the rover counterclockwise by \(X\) degrees.

### Example Command List
```
move forward 10
turn clockwise 90
move forward 5
turn counterclockwise 90
move forward 10
```

## Usage

### Running the Simulation

1. **Save the commands** in a file, e.g., `instructions.txt`.
2. **Run the program** from the command line, specifying the path to the command file:

   ```bash
   python simulate_rover.py path/to/instructions.txt
   ```

### Example Output
The program outputs the rover's position and orientation after each instruction and displays the path in a Turtle graphics window:

```
I'm at (0, 0) facing 0 degrees
Moving 10 meters forward (instruction 1)
I'm at (0, 10) facing 0 degrees
Turning 90 degrees clockwise (instruction 2)
I'm at (0, 10) facing 90 degrees
Moving 5 meters forward (instruction 3)
I'm at (5, 10) facing 90 degrees
Turning 90 degrees counterclockwise (instruction 4)
I'm at (5, 10) facing 0 degrees
Moving 10 meters forward (instruction 5)
I'm at (5, 20) facing 0 degrees
```

### Turtle Visualization
The Turtle graphics window shows the rover's path in real time, with the rover visualized as a turtle icon. Movements and turns are represented on the screen, providing an intuitive view of the rover's navigation.

### Error Handling
If the program encounters an unknown instruction, it stops and displays an error message. It also checks for missing file paths and displays usage instructions.

## Dependencies
- **Python** (3.x)
- **Turtle Graphics** (Standard library in Python)

## License
This project is open-source and available under the MIT License.

--- 

This `README.md` provides comprehensive guidance on setting up and running the simulation, along with descriptions of output and error handling.