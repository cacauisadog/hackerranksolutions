# https://www.hackerrank.com/challenges/one-month-preparation-kit-tower-breakers-1/problem


def towerBreakers(n, m):
    # if height is 1, player 1 automatically loses no matter how many towers.
    if m == 1:
        return 2

    # if there is only one tower (and its height is > 1), player 1 just reduces its height to 1 and player 2 loses
    if n == 1:
        return 1

    # if there is an even number of towers, player 2 always wins:
    # - p1 reduces t1 to 1
    # - p2 reduces t2 to 1
    # - p1 has no more moves. Repeat n times for any even number. If p1 reduces to more than 1, p2 simply does the same
    # to another tower, and we're back to the same situation.
    if n % 2 == 0:
        return 2

    # if there is an odd number of towers, player 1 always wins:
    # - p1 reduces t1 to 1
    # - p2 reduces t2 to 1
    # - p1 reduces t3 to 1
    # - p2 has no more moves. Repeat n times for any odd number. If p2 reduces to more than 1, p1 simply does the same
    # to another tower, and we're back to the same situation.
    return 1


# I will leave this completely unoptimized solution here, because it was super fun to code. It felt like coding an
# extremely simple game, and that's always a plus to me. Too bad it fails on all but 2 tests since it runs so poorly.
# Maybe someday I will turn it into an actual 2 player game using pygame; who knows?


# class Game:
#     def __init__(self, num_towers, height):
#         self.towers = self._build_towers(num_towers, height)
#         self.current_player = "p1"

#     def play(self):
#         while self._has_moves_left():
#             tallest_tower, value = self._find_tallest_tower()
#             if self._is_last_tower_bigger_than_one(tallest_tower):
#                 self.towers[tallest_tower] = 1
#             else:
#                 new_value = self._calculate_new_tower_value(value)
#                 self.towers[tallest_tower] = new_value

#             self._switch_players()

#         if self.current_player == "p1":
#             return 2
#         return 1

#     def _switch_players(self):
#         if self.current_player == "p1":
#             self.current_player = "p2"
#         else:
#             self.current_player = "p1"

#     @staticmethod
#     def _build_towers(num_towers, height):
#         return {t + 1: height for t in range(num_towers)}

#     def _has_moves_left(self, towers=None):
#         if not towers:
#             towers = self.towers

#         towers_heights = towers.values()
#         for height in towers_heights:
#             if height > 1:
#                 return True

#         return False

#     def _find_tallest_tower(self):
#         towers_heights = self.towers.values()
#         tallest_value = max(towers_heights)
#         for tower in self.towers:
#             if self.towers[tower] == tallest_value:
#                 return tower, self.towers[tower]

#     def _is_last_tower_bigger_than_one(self, tower):
#         for t in self.towers:
#             if t != tower and self.towers[t] > 1:
#                 return False

#         return True

#     @staticmethod
#     def _calculate_new_tower_value(value):
#         half = value // 2
#         for i in range(1, half, -1):
#             if value % i == 0:
#                 return i

#         else:
#             return 1


# print(towerBreakers(2, 6))  # 2
# print(towerBreakers(2, 2))  # 2
# print(towerBreakers(1, 4))  # 1
# print(towerBreakers(212387, 779))
