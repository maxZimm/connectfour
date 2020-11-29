Connect Four

Definition:
Connect  four is a board game that involves:
- 2 players
- 6 unit by 7 unit board
- Collection of color coded tokens for each player
  - traditionally colors are red and yellow

Game Play
- Players take turns to make 1 move per turn
- A move is when a player places 1 token into 1 of the 7 columns of the board
- A Player has won when 4 of their tokens are adjacent to each other either vertically, horizontally, or diagonally

Classes 
- IO class to handle user input and game display
- Player to identify who is making a move and how it will be represented on board
- Board keep track of the state of the game, which moves are where
- Game collect all the classes to initiate the game and determine a winner/end the game

Structure of Data
- How should the board class represent the board?
  - Needs to be able to recal a place on the board and whether it is holding player 1 or 2 token. Needs to scan all of itself to 
determine the winner. 
  - Well from the video that guy used lists which seems like a good idea in a way bc you could easily grab things by index
  - But lists are for inserting and extracting too which could easily disrupt the placement of things
  - dictionary feels more premanent, huh turns out you could use numbers as a key to a dictionary
  - so we can make a matrix with dictionary 
  - All in all I think we could use either which is tuff to say why one is better than the other
   
- Player

- Game

- IO
