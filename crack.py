#basically calculate nth number of thue morse, instead of using 0 and 1, we use left and right
stepOnCrack=lambda f,n: ("right","left")[int("l" in f) - bin(n-1).count("1") % 2]
print stepOnCrack("right",6)