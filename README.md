# Sudoku-Game

## Input
* "H" or "h"                
  * Display a help message.
* "Q" or "q"                
  * Stop playing the current game
* "{row} {column} {value}"
  * Insert the value at the specified position. {row} and {column} from 0 to 8, {value} from 1 to 9.
* "{row} {column} C"
  * Clear the cell at the specified position. C must be in upper case.
  
## Example Gameplay
```sh
Please insert the name of a board file: boards/board_x.txt
685|132|947 0
734|598|216 1
219|764|853 2
-----------
926|871|534 3
851|349|672 4
473|256|189 5
-----------
568|427|391 6
342|915|768 7
197|683|42_ 8

012 345 678
Please input your move: 8 8 5
685|132|947 0
734|598|216 1
219|764|853 2
-----------
926|871|534 3
851|349|672 4
473|256|189 5
-----------
568|427|391 6
342|915|768 7
197|683|425 8
012 345 678
Congratulations, you won!
Would you like to start a new game (y/n)? n
```
