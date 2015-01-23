'''
prints the number of times the string 'bob' occurs in s
'''

s = 'bobobobbob'
counter = 0
for s1 in range(0,len(s)+1):
    for s2 in range(s1,len(s)+1):
        if s[s1:s2] == "bob":
            counter += 1
print 'Number of times bob occurs is:', counter

print 1
