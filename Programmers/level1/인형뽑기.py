def solution(board, moves):
    answer = 0
    basket = []
    for move in moves:
        for i in range(len(board)):
            value = board[i][move-1]
            if value != 0:
                basket.append(value)
                board[i][move-1] = 0
                if len(basket) > 1 and basket[-1] == basket[-2]:
                    basket.pop(-1)
                    basket.pop(-1)
                    answer += 2
                break
    return answer