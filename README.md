# badChessEngine
my firts chess game i have ever made in python probably teriable and full of errors. i am new to programing

This is a Chess game made in Python by Ruben Hillier.

Fetures:
Terminal Chess board
All Pices with full ligal movement
Human vs Human only
Castling
En passant
Check
check mate

Fetures to add:
Stail mate 
draw by repetition

How to play this chess engine in steps:
1. You will first be asked column, this is the column of the pice you would like to move.
2. YOu will then be asked Row, this is the row of the pice you would like to move.
3. You will then be tould what pice you chose, if there was no pice at that location it will
tell you and send you back to step 1.
4. If you did select a valid pice then you will be prompted with the column of were you want to move your pice to.
5. Then you will be asked the row position of were you want to move your pice to.
6. If you chose a ligal move then the board will be redrawn with the updated positions and it will be the other 
persons go, if you did not pick a ligal move the board will be redrawn without any changes and it will still be your go.
7. This will keep looping around doing this until one of you ether gets check or check mate. if you get check then you
will be tould so and will only be able to make ligal moves if you dont it will ask you again to make a move without 
updating the board. If its check mate then you will be tould who wone and if you would like to plat again y for yes and
n for no.

If you want to look at the source code its in the foulder source code, the code is in python3.
The Chess.exe file was made using pyinstaller
