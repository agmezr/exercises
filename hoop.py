"""
In a game we called that "hoop", n player numbered from 1 to n are playing. The first player says 1, the second player says 2 and so on. 
After everyone says a number, it's the first player's turn again. 
There's an additional rule that make the game more interesting: 
if the current number the person should say is divisible by 3 or 7, the person should say 0 instead.

You're given the number of players n, the number of turns m the game was played, and what was said in each turn. Your task is to find the players who made mistakes.

the players should be returned in the order they made mistakes;
if the player made several mistakes, all of them should be returned.
"""
hoop = lambda n, m, l: [i%n or n for i in range(1,m+1) if l[i-1]!= (i%3 and i%7 and i) ]

#tests
n= 3
m= 8
turns= [1, 2, 3, 4, 4, 0, 0, 0] # result[3, 2, 2].

print hoop(n,m,turns)
