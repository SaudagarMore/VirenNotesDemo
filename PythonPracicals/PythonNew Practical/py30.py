#python Generator
#return ->one one value and run only one time.
def demo():
    t=1
    while t<=10:
       yield t*t
#       yield t*t*t
       t+=1      

print(list(demo()))
print("-------------------")
for k in demo():
    print(k)