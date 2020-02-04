def win_comb(tic_tac_len):
    #initialize empty winning combinations list
    winning_combinations = []


    #calculate winning rows
    for i in range(tic_tac_len, tic_tac_len*(tic_tac_len+1), tic_tac_len):
        winning_combinations.append({j for j in range(i-tic_tac_len,i,1)})
    

    #calculate winning columns
    for i in range(tic_tac_len*(tic_tac_len-1), tic_tac_len**2, 1):
        winning_combinations.append({j for j in range(i-tic_tac_len*(tic_tac_len-1),i+1,tic_tac_len)})


    #calculate winning diagonals
    winning_combinations.append({i for i in range(0, tic_tac_len**2, tic_tac_len+1)})

    winning_combinations.append({i for i in range(tic_tac_len**2-tic_tac_len, tic_tac_len-2, -(tic_tac_len-1))})

    return(winning_combinations)
