import re

def split_and_cat(obj_str,delim='([-,+,i])',delim_simp=['-','+'],delim_jump=['i']):
    temp_array=[]
    for i in range(len(obj_str)):
        #split
        temp_split = re.split(delim,obj_str[i])
        #cat
        if temp_split[0] == obj_str[i]:
            temp_array.append(temp_split[0])
            continue
        else:
            j=0
            while (j<len(temp_split)):
                if temp_split[j] in delim_simp:
                    temp_array.append(temp_split[j]+temp_split[j+1])
                    j=j+2
                elif temp_split[j] in delim_jump:
                    j=j+1
                elif temp_split[j] == '':
                    j=j+1
                else:
                    temp_array.append(temp_split[j])
                    j=j+1
    return temp_array