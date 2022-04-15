# When You Just Can't Decide

## Background

### The long version:
If you've played DND, AD&D, Shadowrun, Star Wars, or other turn-based role-playing games, or even just any board games that use more than just "regular" six-sided dice, you're likely familiar with myriad other options. There are 4, 6, 8, 10, 12, and 20-sided dice in common use in some games (d4, d6, d8, d10, d12, d20). Gamers already know that if you roll six 20-sided dice, you'd say you're rolling 6d20.

What if we wanted to use a 3-sided die, though? We can't build one in our current physical world/dimension, but we could simulate one physically by taping 1s, 2s, and 3s to a 6-sided die, effectively halving the number of options available. Yeah, we've probably all done it or know someone who has, but that's boring. Alternatively, we can conjure a virtual 1d3 by making a computer simulate randomness to choose for us.

### The short version:
A friend and I wanted to get together for coffee but neither of us cared where we went or wanted to decide until the last minute. He made a joke about flipping a three sided die and I got really, really bored with a Python tutorial that was explaining about what for loops and while loops are and just wanted to figure out how to bend Python's syntax to my will to do things I've already done in other languages. This happened.

## Usage:

Just download and 
```
./1d3.py
```

The rest is self-explanatory.

## Example:
```
bmsnook@Mac-Mini:~/github/1d3% ./1d3.py 
Let the Fates decide for you
Designate 3 choices to roll for: 
Specify choice A: Oak Grove Market
Specify choice B: Einstein Bros Bagels
Specify choice C: Panera
Let's roll less than 10 times so we're not here all day
How many times should I roll? 2

Great, I'll roll 2 times

Consulting the great Oracle "1d3" (really, "2d3") to choose between:
    A :: Oak Grove Market
    B :: Einstein Bros Bagels
    C :: Panera
Rolling...

     ^
    / \
   / A \
  /     \
 / B   C \
/_________\
     ^
    / \
   / B \
  /     \
 / C   A \
/_________\
Results of 2 rolls:
    Rolled A     1 times (Oak Grove Market)
    Rolled B     1 times (Einstein Bros Bagels)
    Rolled C     0 times (Panera)
There are 2 winners: {'A': 1, 'B': 1}
Continuing to roll to break the tie
     ^
    / \
   / A \
  /     \
 / B   C \
/_________\

Results of 3 rolls:
    Rolled A     2 times (Oak Grove Market)
    Rolled B     1 times (Einstein Bros Bagels)
    Rolled C     0 times (Panera)

Your choice is made; the winner is A: Oak Grove Market
bmsnook@Mac-Mini:~/github/1d3% 
```
