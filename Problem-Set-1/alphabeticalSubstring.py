'''prints the longest substring of s 
   in which the letters occur in alphabetical order '''
s = 'azcbobobegghakl'
substring = {}
max_value = 0
for i in range(len(s)):
	count = 0
	sub_value = s[i]
	while i+1 < len(s) and s[i] <= s[i+1]:
		count += 1
		i += 1
		sub_value += s[i]

	substring[count] = substring.get(count, sub_value)
	max_value = max(substring.keys())

print('Longest substring in alphabetical order is: %s' % substring[max_value])
