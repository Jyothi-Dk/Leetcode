s='abcabcbbb'
l=len(s)

list_idx={}

max_length=0

start=0

for end in range(l):
    current_char=s[end]
    start=max(start,list_idx.get(current_char,0))
    #print("start"+str(start))
    max_length=max(max_length,end-start+1) 
    #print(max_length)    
    list_idx[current_char]=end+1

print(max_length)