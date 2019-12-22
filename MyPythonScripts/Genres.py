genreList = ["candy pop", "emo", "pixie", "pop emo", "pop punk", "anthem emo", "pop punk",
             "alternative emo", "anthem emo","emo", "pop punk", "alternative emo",
             "anthem emo", "emo", "midwest emo", "pop punk", "socal pop punk",
             "pop punk", "punk", "socal pop punk", "indie pop", "indie poptimism",
             "indie rock", "indietronica", "minneapolis indie", "modern rock",
             "hopebeat", "indie pop", "indie poptimism", "indie rockism", "indietronica",
             "modern alternative rock", "modern rock", "alternative emo",
             "anthem emo", "emo", "pop punk", "australian pop", "electropop",
             "indie poptimism", "pop", "edm", "electropop", "pop", "catstep", "edm",
             "electropop", "indie electropop", "indie poptimism", "indietronica",
             "new french touch", "pop edm", "swedish electropop", "tropical house",
             "vapor soul", "vapor twitch", "catstep"]

def Remove(duplicate): 
    final_list = [] 
    for num in duplicate: 
        if num not in final_list: 
            final_list.append(num) 
    return final_list 
      
# Driver Code 

print(Remove(genreList)) 
