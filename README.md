# AIPlaysGames
Simple Genetic Algorithms &amp; Deep Learning Based AI Learns How To Play Snake, Breakout, and PacMan.

Team: Nathanael L. Mann, Austin Brown, Cooper Martin

Our team re-created three classic arcade-style games in Python using the Pygame Library; Breakout, Snake, and Pac-Man. We then implemented a neural network to learn each of these games using NumPy and allowed it to learn over time through trial and error. We used a combination of shallow neural networks and deep neural networks and found that the simpler variety was sufficient for Breakout, but that even with the added complexity the deep neural network was not able to achieve a perfect score in either Snake or Pacman.

# To use the program you will need the following:

## The latest version of Python 3
Python 3 Installation Site: https://www.python.org/downloads/

## The latest version of Pip3
Instructions for Installing Pip for Python: https://pip.pypa.io/en/stable/installing/

## An installation of PyGame 
After setting up your Python and Pip installations you will need to install PyGame. Check to make sure your Python and Pip installations are working. 

### On Windows, you will use 
` python3 --version `

### On other systems, you will use 
` python --version `

### The same goes for the Pip installation
` pip3 --version ` for Windows
` pip --version ` for other systems

### If both dependencies are functioning properly you will use the command 
` pip3 install pygame ` for Windows
` pip install pygame ` for Others

Make sure you have an internet connection when installing PyGame.

## An installation of Turtle

The same installation rules go for Turtle. Make sure that the dependencies are functional using the commands above and use the command 
` pip3 install turtle ` for Windows 
` pip install turtle ` for Others

## An installation of NumPy

The same installation rules go for NumPy. Make sure that the dependencies are functional using the commands above and use the command 
` pip3 install numpy ` for Windows 
` pip install numpy ` for Others

## How To Use The Program

To use the program you will need to open a command prompt and change it into the directory that you cloned this repository into. You will need to cd into the src directory and run the command

` python StatReader.py `

This will bring up a menu where you can choose which game you want to run and in which mode you want it to run. You can use the up and down arrow keys to choose the game you want to play, and then use 0 and 1 to go up and down the play method menu. 

Agent Mode -- This will have the game be played by a Simple Reflex Agent.

Neural Network Mode -- This will have the game be played by a Neural Network that is training to play the game.

User Mode -- Will allow you to play the game using the arrow keys.

To end the session, close out of the game by hitting the X in the top right corner of the game window and if the menu hasn't already closed by then, hit the X on that window as well. 
You can also ` CONTROL + C ` or `COMMAND + C` on the console window to terminate it entirely. 
