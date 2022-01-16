# given an integer array, output unique integers that will add up to a specific value k 
#solution 1


def pair_sum(listt, target):
    for num in range(len(listt)-1):
        
        if listt[num] + listt[num+1] == target:
            print((listt[num], listt[num+1]))


pair_sum([1,3,2,2],4)