no=input("Enter any numbeR:")
total_even_sum=0
j=0
while j<len(no):
    digit=int(no[j])
    if digit%2==0:
        total_even_sum+=digit
    j+=1
    
print("Total Sum of Even is:",total_even_sum)