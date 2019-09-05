from pprint import pprint
from characters import characters
from houses import houses

print("START WITH A: ")
charwitha = 0
for character in characters:
    if character['name'][0] == 'A':
        charwitha+=1
print(charwitha)

print("START WITH Z: ")
charwithz = 0
for character in characters:
    if character['name'][0] == 'Z':
        charwithz+=1
print(charwithz)

print("DEAD: ")
chardead = 0
for character in characters:
    if character["died"] != '':
        chardead+=1
print(chardead)


print("TITLES: ")
mosttitles = 0
title = 0
i = 0
for character in characters:
    if(len(character["titles"]) > title):
        mosttitles = i
        title = len(character["titles"])
    i+=1
print(characters[mosttitles]["name"]," has the most titles: ",characters[mosttitles]["titles"])

print("VALERIAN: ")
charval = 0
for character in characters:
    if character["culture"] == 'Valyrian':
        charval+=1
print(charval)

print("HOT PIE ACTOR:")
for character in characters:
    if character["name"] == 'Hot Pie':
        print(character["playedBy"][0])

print("BOOK CHARACTERS: ")
chartv = 0
for character in characters:
    if character["tvSeries"][0] == '':
        chartv+=1
print(chartv)

print("TARGARYENS: ")
targaryen = []
for character in characters:
    if(character["name"].find("Targaryen") >= 0):
        targaryen.append(character["name"])
print(targaryen)



print("HOUSE HISTOGRAM: ")
results = {}
for character in characters:
    for ally in character["allegiances"]:
        results[houses[ally]] = 0
for character in characters:
    for ally in character["allegiances"]:
        results[houses[ally]] +=1

end = results.copy()
sortedresl = []
while len(end)>0:
    top=0
    for house in end:
        if(end[house]>top):
            top=end[house]
    for house in end:
        if(end[house]==top):
            sortedresl.append(house)
            end.pop(house)
            break

for house in sortedresl:
    print(house, " has ", results[house], " allegiances")




# print(len(characters))

# # print out the key names individually
# for k in jon_snow:
#    print(k)

# # print out just the values
# for key in jon_snow:
#    print(jon_snow[key])

# # print both the key and the value
# for k in characters.jon_snow:
#    print("%s: %s" % (k, jon_snow[k]))