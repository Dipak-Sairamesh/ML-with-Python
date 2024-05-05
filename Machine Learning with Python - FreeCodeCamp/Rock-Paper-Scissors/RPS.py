# The example function below keeps track of the opponent's history and plays whatever the opponent played two plays ago. It is not a very good player so you will need to change the code to pass the challenge.

steps = {}

def join_moves(moves):
    """Concatenate a list of moves into a string"""
    return "".join(moves)

def player(prev_play, opponent_history=[]):
    if prev_play != "":
        opponent_history.append(prev_play)

    pattern_length = 3
    guess = "R"  # default guess is Rock

    if len(opponent_history) > pattern_length:
        # Look at the last n moves the opponent made
        recent_moves = join_moves(opponent_history[-pattern_length:])

        # Increment the count for this pattern of recent moves
        steps[join_moves(opponent_history[-(pattern_length+1):])] = steps.get(join_moves(opponent_history[-(pattern_length+1):]), 0) + 1

        # Consider all possible next moves and pick the one the opponent is most likely to play based on history
        potential_next_moves = [recent_moves + "R", recent_moves + "P", recent_moves + "S"]
        for pattern in potential_next_moves:
            steps[pattern] = steps.get(pattern, 0)

        predicted_opponent_move = max(potential_next_moves, key=lambda key: steps[key])[-1]

        # Play the move that beats the predicted opponent move
        counter_moves = {"R": "P", "P": "S", "S": "R"}
        guess = counter_moves[predicted_opponent_move]

    return guess

