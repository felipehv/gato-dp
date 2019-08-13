from itertools import combinations
from numpy import argmax
# Playing gato is the same as playing 15
"""
|8|3|4|
|1|5|9|
|6|7|2|
"""

WIN = [(1, 5, 9), (1, 6, 8), (2, 4, 9), (2, 5, 8), (2, 6, 7), (3, 4, 8), (3, 5, 7), (4, 5, 6)]

s = {"player": [], "bot": [], "left": [i for i in range(1,10)]}


"""
Predecision
Given an state S, I choose x on all left space

V(S) = max{0, 1, max_x(  ) }
"""

def recursion(player, bot, left, d):
    """
    Bellman recursion
    """
    # Pre state given a player move
    # Check if player won
    if len(player) > 2:
        player_trios = list(filter(lambda x : sum(x) == 15, combinations(player, 3)))
        if len(player_trios) > 0:
            return -len(player)

    # Check if no more moves
    if left == []:
        return 0

    # Post state giving an x choice
    vtgs = []
    for x in left:
        bot_pre = bot.copy()
        bot_pre.append(x)
        # Check if bot won
        if len(bot_pre) > 2:
            bot_trios = list(filter(lambda x : sum(x) == 15, combinations(bot_pre, 3)))
            if len(bot_trios) > 0:
                d['value'] = x
                return len(left)-1

        # Values-to-go for next pre state
        vtgs.append(sum([recursion(player + [y], bot_pre, list(filter(lambda l : l != x and l != y, left)), d) for y in left if y != x ]))

    # Return the chosen value
    argmax_left = argmax(vtgs)
    d['value'] = left[argmax_left]
    return vtgs[argmax_left]
        
        
if __name__ == "__main__":
    Player= []
    Bot= []
    Left= [1,2,3,4,5,6,7,8,9]
    x = {'value': 0}
    print(recursion(Player, Bot, Left, x), x)