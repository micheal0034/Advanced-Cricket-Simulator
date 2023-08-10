# Cricket Simulation Game

This is a cricket simulation game implemented in Python. It simulates a cricket match between two teams and provides a textual representation of the game's progress, including the description of each ball, team scores, wickets, and the final result.

## Methodology

The simulation follows a basic cricket match structure, with each team having a batting and bowling phase. The outcome of each ball played by the batsman against the bowler is determined by their respective skills, pitch conditions, and a random factor. The simulation keeps track of the total score, wickets, and overs for each team. The game continues for a specified number of overs, and the team with the higher score at the end wins.

## Requirements

- Python 3.x

## How to Run

1. Clone or download this repository.
2. Open a terminal or command prompt and navigate to the directory containing the `app.py` file.
3. Run the following command to start the cricket simulation:

```bash
python app.py
```

The simulation will run, and you'll see the progress of the match in the terminal. The output will include information about each ball, the scores, wickets, overs, and the final result of the match.

Here are step-by-step instructions on how to clone, navigate, and run the cricket simulation code:

1. **Clone the Repository**:
    - Open your preferred web browser and go to the GitHub repository containing the cricket simulation code.
    - Click on the "Code" button near the top-right of the repository's page.
    - Choose the "Download ZIP" option to download the repository as a ZIP file.
    - Save the ZIP file to a location on your computer where you'd like to work on this project.
    - Extract the contents of the ZIP file to a folder of your choice.

2. **Open a Terminal or Command Prompt**:
    - On Windows: Press `Win + R`, type `cmd`, and press Enter.
    - On macOS: Press `Command + Space`, type `terminal`, and press Enter.
    - On Linux: Press `Ctrl + Alt + T`.

3. **Navigate to the Directory Containing `app.py`**:
    - Use the `cd` command to change the current directory in the terminal.
    - If you extracted the repository ZIP file to the `Downloads` folder, the command might look like this (replace `<path_to_folder>` with the actual path to the extracted folder):

    ```bash
    cd /path_to_folder/cricket-simulation-game-main
    ```

    - Verify that the `app.py` file is located in this directory by using the `ls` command (on macOS and Linux) or the `dir` command (on Windows):

    ```bash
    ls
    ```

    or

    ```bash
    dir
    ```

4. **Run the Cricket Simulation**:
    - Once you're in the directory containing the `app.py` file, you can run the simulation by executing the following command:

    ```bash
    python app.py
    ```

    - This command runs the Python script, which starts the cricket simulation.
    - You should see the simulation progress in the terminal, displaying information about the match's progress, such as balls played, runs scored, wickets, overs, and the final result.

That's it! You've successfully cloned the repository, navigated to the directory, and run the cricket simulation. Enjoy the game and observe how the match unfolds based on the provided code!

## File Structure

The code is organized into several Python modules:

- `app.py`: This is the main script that creates fake player data, initializes teams, field conditions, and starts the match simulation.
- `player.py`: Defines the `Player` class, representing a cricket player with various skills and attributes.
- `team.py`: Defines the `Team` class, representing a cricket team with players, captain, batting order, and bowlers.
- `field.py`: Defines the `Field` class, representing the field conditions, such as size, pitch conditions, fan ratio, and home advantage.
- `umpire.py`: Defines the `Umpire` class, representing the match umpire who tracks scores, wickets, and overs and predicts the outcome of each ball.
- `commentator.py`: Defines the `Commentator` class, providing descriptions of the match, balls, and other events.

## Customization

You can customize the simulation by adjusting the parameters in the `app.py` file, such as the number of players, the total number of overs, and the skills of the players.

## Enjoy the Game!

That's it! You're ready to run the cricket simulation and enjoy the game. Watch the match unfold in the terminal and see which team emerges victorious. Have fun playing and experimenting with different parameters to explore the dynamics of the game!
