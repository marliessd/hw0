# open file
f = open('iowa-liquor-sample.csv', 'r')
counter = 0
# iterate over all the lines in the file
for line in f:
	# check whether the line contains the phrase
    if 'single malt scotch' in line.lower():
        counter = counter + 1
print 'Number of records containing phrase :',counter