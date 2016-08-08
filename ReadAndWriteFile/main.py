fw = open('sample.txt', 'w')    #open sample.text then write to it.
fw.write('Writing some stuff on my text file\n')
fw.write('I like bacon\n')
fw.close()

fr = open('sample.txt', 'r')    #open sample.text then read it.
text = fr.read()
print(text)
