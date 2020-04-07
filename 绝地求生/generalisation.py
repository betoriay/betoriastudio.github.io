def stimulated(all_killing_lst, cheaters_id, cheaterdic):
    '''Take three inputs, a nested list representing 
    all killing relatonships within the game; 
    two constant value, a cheater_id list and a cheater dictionary
    Return a stimulated nested list within this game'''
    import numpy as np
    import random as ran


    #change it into numpy.ndarray
    original_nw = np.array(all_killing_lst) 
    # create a list to find and store all non_cheaters within this game
    unique_nc = [] 
    gm_cheater = [] # just a intermediary
    all_player = [] #just a intermediary
    for m in all_killing_lst:
        all_player.extend((m[1], m[2]))                   
        for i in range(1, 3):
            if m [i] in cheaters_id and m[3] >= cheaterdic[m[i]]:
                gm_cheater.append(m[i])
                          
    # create a list to store all unique player for this game
    unique_player = list(set(all_player))
    # store the cheater for this game into a list
    unique_gm_cheater = list(set(gm_cheater))
                          
    for player in unique_player:
        if player not in unique_gm_cheater:
            unique_nc.append(player)   
            
    # get all non_cheater and its positions
    nonch_dic = {k:np.where(original_nw == k) for k in unique_nc} 
    
    # shuffle-all-non-cheater and assign them to different positions
    nonch_pos = list(nonch_dic.values())
    # duplicate before shuffle
    nc_copy = unique_nc[:] 
    ran.shuffle(nc_copy)
    new_position = dict(list(zip(nc_copy, nonch_pos)))
    
    # create a stimulated game
    for (k, v) in new_position.items():
        original_nw[v] = k 
        # all non_cheater will change their positions after the loop
    return original_nw.tolist()