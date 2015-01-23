'''
counts up the number of vowels contained in the string s
'''

s = "azcbobobegghakl"
counter = 0
for c in s:
	if c == 'a' or c == 'e' or c == 'i' or c =='o' or c == 'u':
		counter += 1
print 'Number of vowels: ', counter		
