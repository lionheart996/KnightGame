Chess is the oldest game, but it is still popular these days. You will use only one chess piece - the Knight.
A chess knight has 8 possible moves it can make. It can move to the nearest square but not on the same row, column, or diagonal. (e.g., it can move two squares horizontally, then one square vertically, or it can move one square horizontally then two squares vertically - i.e., in an "L" pattern.) 
The knight game is played on a board with dimensions N x N.
You will receive a board with a "K" for knights and a "0" for empty cells. Your task is to remove knights until no knights that can attack one another with one move are left. 
Always remove the knight who can attack the greatest number of knights. If there are two or more knights with the same number of attacks, remove the top-left one.
Input
On the first line, you will receive integer  - the size of the board
On the following (numer of rows in the chess board) lines, you will receive strings with "K" and "0" where "K" is a postion of a knight and "0" is an emptry square.
