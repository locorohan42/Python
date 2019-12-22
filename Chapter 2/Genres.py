genreList = ["candy pop", "emo", "pixie", "pop emo", "pop punk", "anthem emo", "pop punk",
             "alternative emo", "anthem emo","emo", "pop punk", "alternative emo",
             "anthem emo", "emo", "midwest emo", "pop punk", "socal pop punk",
             "pop punk", "punk", "socal pop punk", "indie pop", "indie poptimism",
             "indie rock", "indietronica", "minneapolis indie", "modern rock"]

def Remove(duplicate): 
    final_list = [] 
    for num in duplicate: 
        if num not in final_list: 
            final_list.append(num) 
    return final_list 
      
# Driver Code 

print(Remove(genreList)) 
