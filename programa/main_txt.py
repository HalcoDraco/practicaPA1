from abs_board import board_setup
from constants import *

print("Elige una variante:")
print()
for i, v in enumerate(variants):
    print(str(i+1) + '- ' + v + ':')
    print(variant_descriptions[i])
    print()

end_checker, move = board_setup()
num_players = 2
end = False
while not end:
    for p in range(num_players):
        i, j = move(p)
        end, win, lose = end_checker()
        if end:
            print(win, lose)
            break