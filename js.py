def jewels(S, J):
    jewels = {x: 0 for x in J}
    for char in S:
        if char in jewels.keys():
            jewels[char] += 1
    return print(sum(jewels.values()))
J = "aZAb"
S = "aAAizbbbbc"
jewels(S,J)

