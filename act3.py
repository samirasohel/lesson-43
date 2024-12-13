def contodict(lst):
    result={}
    for item in lst:
        result[item[0]]=item[1:]

    return result
lst1=[['1','samira','2'],['2','sohel','3'],['3','othoi','4']]
print("The list is",lst1)

print("converted dictionary is",contodict(lst1))