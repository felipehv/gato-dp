# GatoDP
Dynamic programming implementation of Tic-Tac-Toe (gato)

## Introduction

This TicTacToe game is implemented as a [sum 15 game.](http://www.ms.uky.edu/~lee/ma310sp15/gameoffifteen.pdf)

There are same amount of trios in a set 1 to 9, that sum 15, as the combinations of trios in a tic-tac-toe game.

The configuration of the square should be something like this.

| | | |
|-|-|-|
|8|3|4|
|1|5|9|
|6|7|2|

## Implementation

### States

The state of the bellman recursion is as follows

```
S = {player, bot, left}
```
Where `player` are all the numbers (or moves) selected by the player at the time of looking at the state. Same for the bot.

The `left` set are all the moves available to be played.

### Decision

The decision of the bot is the play that it makes in a given state S. It can select any number (position) in the `left` set.

### Terminal State

There are two cases:

* The player has one trio in his `player` set that sums 15.
* The bot gets a trio in his `bot` set.
* There are no more moves in the `left` set.

### Rewards

The rewards are, in the first terminal state, the negative of the amount of moves of the player. This is `-len(player set)`.

Then in the second case, the reward will be positive, and equals to the amount of moves available in the `left` set.
This is `len(left set)` after the bot move.

If there are no more moves, the terminal state will reward 0.

### Objective

The objective function is to maximize the score obtained by the bot.
