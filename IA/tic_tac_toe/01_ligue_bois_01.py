import sys
import numpy as np  # available on coding game

k_player = -2
k_opponent = -1

# the cells contain the players' labels or the number of alignments in which they can be included
board_game = np.array([[3, 2, 3], [2, 4, 2], [3, 2, 3]])

diag1_indices = [0, 1, 2]
diag2_indices = [2, 1, 0]


# -----------------------------------------------------------------------------
# L'adversaire pose son jeton en y, x
def update_board_game(opp_row, opp_col):
    # Tout premier tour
    if opp_row == -1 and opp_col == -1:
        print(f"Board at init         :\n{board_game}", file=sys.stderr, flush=True)
        return
    else:
        # Si dans la opp_row, la opp_col ou la diag il n'y a pas déjà de k_opponent alors on enlève 1 aux cellules dont la valeur est > 0
        # En effet on a plus moyen de faire une ligne, une col ou une diag
        # TODO : faudrait pas mettre carrément la cellule à 0 ?
        if k_opponent not in board_game[:, opp_col]:
            board_game[:, opp_col] -= (board_game[:, opp_col] > 0).astype(int)  # astype convert bool to int

        # Ligne
        if k_opponent not in board_game[opp_row]:
            board_game[opp_row] -= (board_game[opp_row] > 0).astype(int)  # astype convert bool to int

        # Si k_opponent n'est pas dans la diagonale principale
        if (opp_row == opp_col) and k_opponent not in board_game[diag1_indices, diag1_indices]:
            board_game[diag1_indices, diag1_indices] -= (board_game[diag1_indices, diag1_indices] > 0).astype(int)

        # Si k_opponent n'est pas dans la diagonale secondaire
        if (opp_row == 2 - opp_col) and k_opponent not in board_game[diag2_indices, diag1_indices]:
            board_game[diag2_indices, diag1_indices] -= (board_game[diag2_indices, diag1_indices] > 0).astype(int)

        # -----------------------------
        # -----------------------------
        # -----------------------------
        # On pose le jeton de l'adversaire
        board_game[opp_row][opp_col] = k_opponent

        # -----------------------------
        # -----------------------------
        # -----------------------------
        # Si dans la ligne, la col ou la diag il y a 2 opponents on ajoute 100 à la cellule restante qui contient une valeur pour la rendre plus attractive
        # Avec +100 on décide de bloquer l'adversaire
        count = np.sum(board_game[:, opp_col] == k_opponent)
        if count == 2:
            board_game[:, opp_col] += 100 * (board_game[:, opp_col] > 0).astype(int)

        # Ligne
        count = np.sum(board_game[opp_row] == k_opponent)
        if count == 2:
            board_game[opp_row] += 100 * (board_game[opp_row] > 0).astype(int)

        # diagonale principale
        count = np.sum(board_game[diag1_indices, diag1_indices] == k_opponent)
        if count == 2:
            board_game[diag1_indices, diag1_indices] += 100 * (board_game[diag1_indices, diag1_indices] > 0).astype(int)

        # diagonale secondaire
        count = np.sum(board_game[diag2_indices, diag1_indices] == k_opponent)
        if count == 2:
            board_game[diag2_indices, diag1_indices] += 100 * (board_game[diag2_indices, diag1_indices] > 0).astype(int)

        print(f"Board after opponent  :\n{board_game}", file=sys.stderr, flush=True)
        return


# -----------------------------------------------------------------------------
def get_best_move() -> tuple[int, int]:

    # On va poser notre jeton en y, x
    max_value = -100
    for j in range(3):
        for i in range(3):
            if board_game[j][i] > max_value:
                max_value = board_game[j][i]
                y = j
                x = i

    # Si dans la ligne, la col ou la diag il y a déjà un de nos jetons on ajoute 1 à la cellule restante qui contient une valeur pour la rendre plus attractive
    # En effet au prochain coup on peut aligner 3 cellules
    if k_player in board_game[:, x]:
        board_game[:, x] += (board_game[:, x] > 0).astype(int)

    if k_player in board_game[y]:
        board_game[y] += (board_game[y] > 0).astype(int)

    if (y == x) and k_player in board_game[diag1_indices, diag1_indices]:
        board_game[diag1_indices, diag1_indices] += (board_game[diag1_indices, diag1_indices] > 0).astype(int)

    if (y == 2 - x) and k_player in board_game[diag2_indices, diag1_indices]:
        board_game[diag2_indices, diag1_indices] += (board_game[diag2_indices, diag1_indices] > 0).astype(int)

    # On pose notre jeton
    board_game[y][x] = k_player

    print(f"Board after selection :\n{board_game}", file=sys.stderr, flush=True)
    return y, x


# -----------------------------------------------------------------------------
while True:
    opponent_row, opponent_col = [int(i) for i in input().split()]
    print(f"{opponent_row} {opponent_col}", file=sys.stderr, flush=True)

    valid_action_count = int(input())
    map_in = [list(map(int, input().split())) for _ in range(valid_action_count)]
    # print(f"{map_in}", file=sys.stderr, flush=True)

    update_board_game(opponent_row, opponent_col)
    y, x = get_best_move()
    print(f"{y} {x}", file=sys.stderr, flush=True)
    print(f"{y} {x}")


# indices = {0, 1, 2}

# line0 = board_game[0]
# line1 = board_game[1]
# line2 = board_game[2]

# col0 = [board_game[0][0], board_game[1][0], board_game[2][0]]
# col1 = [board_game[0][1], board_game[1][1], board_game[2][1]]
# col2 = [board_game[0][2], board_game[1][2], board_game[2][2]]

# col0 = board_game[:, 0]  # reference. Possible car on utilise un np.array
# col1 = board_game[:, 1]
# col2 = board_game[:, 2]

# diag0 = [board_game[0][0], board_game[1][1], board_game[2][2]]
# diag1 = [board_game[0][2], board_game[1][1], board_game[2][0]]
# diag1_indices = np.arange(board_game.shape[0])  # Indices (0,0), (1,1), (2,2)
# diag2_indices = np.arange(board_game.shape[0])[::-1]  # Indices (2,0), (1,1), (0,2)


# The 2 lines below works fine if size if big (1000 vs 3 for example). See scrapbook.ipynb
# next() get the next value of the iterator
# max_value = max(map(max, board_game))
# max_indices = next((i, row.index(max_value)) for i, row in enumerate(board_game) if max_value in row)
# board_game[max_indices[max_indices[1]]][max_indices[0]]= k_player

# max_indices = np.argwhere(board_game == board_game.max())[0]
# board_game[max_indices[1], max_indices[0]]= k_player
# print(f"Board after selection :\n{board_game}", file=sys.stderr, flush=True)

# return max_indices[1], max_indices[0]
