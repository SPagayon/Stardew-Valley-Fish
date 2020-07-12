import json

fishes = {}

'''
Read from input file and parse 
'''

f_name = 'fish.txt'
infile = open(f_name, 'r')

for line in infile:
    line = line.strip()

    if line == '<li>':
        next(infile)
        src = next(infile).strip().split('"')
        if src[0] == 'src=':
            img = src[1].split(' ')[0]
            fish = next(infile).strip()[2:]
            fishes[fish] = img
infile.close()

'''
Write to JSON file 
'''

with open('fish.json', 'w') as outfile:
    json.dump(fishes, outfile)
