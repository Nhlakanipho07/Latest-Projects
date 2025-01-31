def combine(list_1,list_2):
    combined_lists = []
    
    if list_1 != [] and list_2 != []: 
        for combine_lists_index in range(min(len(list_1),len(list_2))):
            combined_lists.append(list_1[combine_lists_index])
            combined_lists.append(list_2[combine_lists_index])
                                
        if max(len(list_1),len(list_2)) == len(list_1):
            combined_lists.extend(list_1[combine_lists_index + 1:])        
        else:
            combined_lists.extend(list_2[combine_lists_index + 1:])
    elif list_1 == [] and list_2 != []:
        combined_lists += list_2
    elif list_2 == [] and list_1 != []:
        combined_lists += list_1       
            
    return combined_lists
