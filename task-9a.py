grades=[85,90,12,53]
print("grades list:",grades)
try:
    index=int(input("enter the index:"))
    print("the grade index",index)
except indexerror:
    print("invalid index and please enter the valid index")
except valueindex:
    print("Invalid input. Please enter a numerical index.")
