from PIL import ImageColor
f = open('gtk.css', 'r')
colorDict = {}
counter = 0


name = input('Enter the theme name: ')
filename = '%s.json' % name
output = open(filename, 'a')
output.write('{\n\t"name": "' + name + '",')
output.write('\n\t"variables": {')

for line in f:
    splitThings = []
    if line[0] == "@":
        splitThings = line.split(" ")
        splitThings[2] = splitThings[2].replace(';','')
        if not splitThings[2][0] == '@':
            colorDict[splitThings[1]] = 'rgb' + str(ImageColor.getcolor(splitThings[2], 'RGB'))
        else:
            colorDict[splitThings[1]] = splitThings[2].replace('\n', '')
        output.write('\n\t\t"' + splitThings[1] + '": "' + colorDict[splitThings[1]] + '",')
    else:
        if counter == 0:
            output.write('\n')
            output.write('\t"custom_css": {')
            output.write('\n\t\t"gtk-4": {"' + '\n')

        line.replace('\n','')

        output.write(line.rstrip('\n') + '\\' + 'n')
        counter += 1

output.write('"'.rstrip('\n'))
output.write('\n\t}')
output.write('\n}')

f.close()
output.close()
output = open(filename, 'r')
print(output.read())
