def counter(killing_lst, cheater_lst):
    '''Recieve two parameters: one nested list representing killings within each game,
    one constant list(including cheater_id);
    Return a integer representing the amount of victim-cheater motifs '''
    
    # Create Dictionaries to group all 'interesting killings action' by match-id
    # Therefore, an empty dictionary is created where key is the unique match-id numbers
    # Create a dictionary to store cheaters id and their start cheating time
    # Create a list for cheater dictionary key -- cheater_id_account
    cheaters_id = []
    for i in range(len(cheater_lst)):
        cheaters_id.append(cheater_lst[i][0])
        # len(cheaters_id) == len(set(cheaters_id)), the result is TRUE
        # Therefore, there is no duplicated cheaters.
        
    # Create a list for cheater dictionary value -- cheated_time
    cheaters_tm = []
    for i in range(len(cheater_lst)):
        cheaters_tm.append(cheater_lst[i][1])
    
    cheaterdic = dict(zip(cheaters_id, cheaters_tm))
    
    unique_gm = []
    
    for i in range(len(killing_lst)):
        game_id = killing_lst[i][0]
        unique_gm.append(game_id)
    
    unique_match_gameid = list(set(unique_gm))

    game_dic = {k: [] for k in unique_match_gameid}
    
    # find killing action in each match game that satisfying 
    # 'the killer is also the cheater', which means:
    # 1)killers are also cheaters
    # 2)the killers killing time should not be later than the cheating started time
    
    for sample_killers in killing_lst:  
        if sample_killers[1] in cheaters_id and sample_killers[3] >= cheaterdic[sample_killers[1]]:
            game_dic[sample_killers[0]].append(sample_killers[1:4])
            
    # create a new list to store the output
    poor_guy_kill = []
    for i in unique_match_gameid:
        poor_guy_kill.extend(game_dic[i])
        # the poor_guy_kill list is a nested list
        # which includes all cheater killers in our sample.
        
    # select the victim–cheater motifs
    # filter from the poor_guy_kill list that satisfying these two criteria:
    # 1)victim who is also in the cheater_lst
    # 2)the time this victim become cheater is within the following five days of being killed

    # create an empty list for victim-cheater motifs first
    vcm_lst = []
    import timecounter

    for p_vcm in poor_guy_kill:
        
        #tk = p_vcm[2]
        #tc = cheaterdic[p_vcm[1]]
        if p_vcm[1] in cheaters_id and 0 <= timecounter.day_interval(p_vcm[2], cheaterdic[p_vcm[1]]) <= 4:
            vcm_lst.append(p_vcm[1])
        
    print('The amount of that victim–cheater motifs is', str(len(vcm_lst))+".") 