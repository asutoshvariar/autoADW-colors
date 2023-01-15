from PIL import ImageColor

# Open in-folder gtk.css
f = open('gtk.css', 'r')
colorDict = {}
counter = 0
what = 0

# User defined
name = input('Enter the theme name: ')
filename = '%s.json' % name
output = open(filename, 'a')
output.write('{\n    "name": "' + name + '",')
output.write('\n    "variables": {')

# For loop
for line in f:
    splitThings = []
    # Checks to see if line is defining color
    if line[0] == "@":
        splitThings = line.split(" ")
        splitThings[2] = splitThings[2].replace(';','')
        if not splitThings[2][0] == '@':
            colorDict[splitThings[1]] = 'rgb' + str(ImageColor.getcolor(splitThings[2], 'RGB'))
            output.write('\n        "' + splitThings[1] + ': "' + colorDict[splitThings[1]] + '",')
        else:
            if splitThings[1] == 'error_color':
                colorDict[splitThings[1]] = colorDict[splitThings[2].replace('@','').strip()]
                output.write('\n        "' + splitThings[1] + '": "' + colorDict[splitThings[1]] + '"')
            else:
                colorDict[splitThings[1]] = colorDict[splitThings[2].replace('@','').strip()]
                output.write('\n        "' + splitThings[1] + '": "' + colorDict[splitThings[1]] + '",')
    else:
        if counter == 0:
            output.write('\n    },')
            output.write('\n')
            output.write('    "custom_css": {')
            output.write('\n        "gtk-4": "')

        line.replace('\n','')

        output.write(line.rstrip('\n') + '\\' + 'n')
        counter += 1

output.write('"'.rstrip('\n'))
output.write('\n    }')
output.write('\n}')

f.close()
output.close()
output = open(filename, 'r')
print(output.read())
