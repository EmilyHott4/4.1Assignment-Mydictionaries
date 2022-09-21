#def main():
textFile = "text.txt"
textFile = open(textFile, "r")
textFile = open(textFile, "w")
Dict = wordCount (textFile)
display (Dict)
    

#def word_count (textfile):
Dict = {}
    #text = open(textFile, "r")
lines - textFile.readlines()
for line in lines:
    Word + line.split()
    for word in Word: 
        if word in Dict:
            Dict[word] += 1
        else:
            Dict[word] = 1
#return Dict
#def display (Dict):
for key in Dict:
    print(key, ",", Dict[key])


#main()