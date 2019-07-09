points_per_position = {"1": 25, "2": 18, "3": 15, "4": 12,
                       "5": 10, "6": 8, "7": 6, "8": 4, "9": 2, "10": 1, "R": 0}
# Roseberg left, Hamilton right
Rosberg_Hamilton_score = [["AUS", "1", "2"], ["BHR", "1", "3"], ["CHN", "1", "7"], ["RUS", "1", "2"], ["ESP", "R", "R"], ["MON", "7", "1"], ["CAN", "5", "1"], ["EUR", "1", "5"], ["AUT", "4", "1"], [
    "GBR", "3", "1"], ["HUN", "2", "1"], ["GER", "4", "1"], ["BEL", "1", "3"], ["ITA", "1", "2"], ["SIN", "1", "3"], ["MAL", "3", "R"], ["JPN", "1", "3"], ["USA", "2", "1"], ["MEX", "2", "1"], ["BRA", "2", "1"], ["ABU", "2", "1"]]

# Add some blank spaces before the start
for x in range(5):
    print("")

print("------------------------------------------------------------------------------------")
print("{:^84}".format("Overview of the 2016 F1 World Championship"))
print("------------------------------------------------------------------------------------")
print("────────────────────────────────────────────────────────────────────────────────────")
print("| Grand Prix Location | Nico Rosberg | Lewis Hamilton | Point Difference (Rosberg) |")
print("────────────────────────────────────────────────────────────────────────────────────")

Rosberg_points = 0
Hamilton_points = 0

for score in Rosberg_Hamilton_score:
    Rosberg_points = Rosberg_points + points_per_position[score[1]]
    Hamilton_points = Hamilton_points + points_per_position[score[2]]
    print(
        "| {:^19} | ({}) {:^8} | ({}) {:^10} | {:^+26} |".format(score[0], score[1], Rosberg_points, score[2], Hamilton_points, Rosberg_points - Hamilton_points))
print("────────────────────────────────────────────────────────────────────────────────────")
