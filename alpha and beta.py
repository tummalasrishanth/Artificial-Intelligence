def alphabeta(depth, node_index, maximizingPlayer, values, alpha, beta):
    if depth == 3:
        return values[node_index]
    if maximizingPlayer:
        max_eval = float('-inf')
        for i in range(2): 
            eval = alphabeta(depth + 1, node_index * 2 + i, False, values, alpha, beta)
            max_eval = max(max_eval, eval)
            alpha = max(alpha, eval)
            if beta <= alpha:
                break  
        return max_eval
    else:
        min_eval = float('inf')
        for i in range(2):
            eval = alphabeta(depth + 1, node_index * 2 + i, True, values, alpha, beta)
            min_eval = min(min_eval, eval)
            beta = min(beta, eval)
            if beta <= alpha:
                break  
        return min_eval
values = [3, 5, 6, 9, 1, 2, 0, -1]
optimal_value = alphabeta(0, 0, True, values, float('-inf'), float('inf'))
print("The optimal value is:", optimal_value)