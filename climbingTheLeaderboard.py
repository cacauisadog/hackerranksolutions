def climbingLeaderboard(ranked, player):
    players_rank: list[int] = []
    ranked_set = list(dict.fromkeys(ranked))

    i = len(ranked_set) - 1

    for p in player:
        if p > ranked_set[0]:
            players_rank.append(1)

        else:
            while i >= 0:
                if p == ranked_set[i]:
                    players_rank.append(i + 1)
                    break
                elif p < ranked_set[i]:
                    players_rank.append(i + 2)
                    break
                else:
                    i -= 1

    return players_rank


print(climbingLeaderboard([100, 90, 90, 80, 75, 60], [50, 65, 77, 90, 102]))
