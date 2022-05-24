import random
from random import shuffle
def scramble_items(sample_list): 
    ''' 
    [item, item,... ,item] -> [str, str,... ,str] 
 
Input: list of items that could be int, float, or string. 
Output: list of scrambled strings. 
'''
    newlist = []
    for i in range(len(sample_list)):
        x = str(sample_list[i])
        final_x = (x[1::2]) + (x[::2])
        newlist.append(final_x)
    return newlist


def write_scrambled_items(filename,data):

    fout = open(filename,'w')
    
    for item in data:

        line = scramble_items(item)

        line = ','.join(line)

        fout.write(line +'\n')
       
    fout.close()


def calc_averages(lab_grades): 
    ''' 
    [[str,...,str],[num,...,num], ...] -> [[str, str],[num, num], ...] 
     
    Input: a nested list of strings and integers representing field names, student 
ids and lab grades which may have ‘e’ included. 
 
    Output: nested list containing the student ID and average grade on the labs 
calculated by excluding exemptions 'e' and lowest lab grade in the computation. 
    '''
    final_list=[['Student ID','Average Grade']] 
    for i in range(1,len(lab_grades)): 
        templist=[grade for grade in lab_grades[i] if(type(grade)==int)] 
        templist.remove(min(templist)) 
        avg=sum(templist[1:])/(len(templist)-1) 
        id_avg=[templist[0],avg] 
        final_list.append(id_avg) 
    return final_list 
        
    
 
 
        
            
                
            
        
 
