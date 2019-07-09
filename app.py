points_per_position = {"1": 25, "2": 18, "3": 15, "4": 12,
                       "5": 10, "6": 8, "7": 6, "8": 4, "9": 2, "10": 1, "Ret": 0}
# Roseberg left, Hamilton right
Rosberg_Hamilton_score = [["AUS", "1", "2"], ["BHR", "1", "3"], ["CHN", "1", "7"], ["RUS", "1", "2"], ["ESP", "Ret", "Ret"], ["MON", "7", "1"], ["CAN", "5", "1"], ["EUR", "1", "5"], ["AUT", "4", "1"], [
    "GBR", "3", "1"], ["HUN", "2", "1"], ["GER", "4", "1"], ["BEL", "1", "3"], ["ITA", "1", "2"], ["SIN", "1", "3"], ["MAL", "3", "Ret"], ["JPN", "1", "3"], ["USA", "2", "1"], ["MEX", "2", "1"], ["BRA", "2", "1"], ["ABU", "2", "1"]]

print("--------------------------------------------------------")
print("           Welcome to the 2016 F1 Championship          ")
print("--------------------------------------------------------")
print("───────────────────────────────────────────────────────────────────────────")
print("| Grand Prix Location | Nico Roseberg | Lewis Hamilton | Point Difference |")
print("───────────────────────────────────────────────────────────────────────────")

Roseberg_points = 0
Hamilton_points = 0

for score in Rosberg_Hamilton_score:
    Roseberg_points = Roseberg_points + points_per_position[score[1]]
    Hamilton_points = Hamilton_points + points_per_position[score[2]]
    print(
        f"          {score[0]}               ({score[1]}) {Roseberg_points}               ({score[2]}) {Hamilton_points}        {Roseberg_points - Hamilton_points}")

print("───────────────────────────────────────────────────────────────────────────")
