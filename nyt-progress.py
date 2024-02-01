
# python script to create strings of Puzzle IDs to query NYTimes Crossword 
# Then read the result to find which puzzles have been started but not completed

import json

# nyt api query + add on all IDs (max 1000 per request)
query = "https://www.nytimes.com/svc/crosswords/v3/86120152/progress.json?puzzle_ids="
for id in range(11000, 12000):
    query += str(id) + ','

print(query)
# quit() in case you only want to get the query and not read the file

# you must manually copy/paste result from api to a file and then read said file making sure it is just a list of objects 
with open('file.json', 'r') as f:
    data = json.loads(f.read())

i = 0 # number of puzzles found to complete 
# get every started but not completed puzzle and print it out
for crossword in data:
    if crossword['publish_type'] == 'Daily' and crossword['solved'] == False and crossword['star'] != 'Gold':
        print(crossword)
        i += 1        
print(i)



