'''
Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Aliquet eget sit amet tellus. Sit amet nulla facilisi morbi tempus iaculis urna id. Tellus pellentesque eu tincidunt tortor aliquam nulla. Faucibus turpis in eu mi bibendum neque egestas congue quisque. Quis lectus nulla at volutpat diam. Non odio euismod lacinia at quis risus sed. Integer eget aliquet nibh praesent tristique magna. Volutpat diam ut venenatis tellus in metus. In fermentum et sollicitudin ac orci phasellus egestas. Varius duis at consectetur lorem donec massa sapien. Et leo duis ut diam.
'''

text = str(input("-Please enter the text-\n"))

#Analyz parameters
listOfText = text.split()
numberOfWords = len(listOfText)
numberOfChars = len(text)

#Calculating frequency of words
wordFrequency = {}
for word in listOfText:
    if word not in wordFrequency.keys():
        frequencyOfWord = 0
        for i in range(len(listOfText)):
            # if(i == listOfText.index(word)): frequencyOfWord = 1 olsaydı bu kod parçası çalışmalıydı
            #     continue
            if word == listOfText[i]: #Boyle olursa kucuk buyuk duyarlılığı olur
                frequencyOfWord += 1
            wordFrequency[word] = frequencyOfWord

sortedFrequencies = dict(sorted(wordFrequency.items(), key=lambda x: x[1]))


print("\nList of text: ", listOfText)
print("\nNumber of words: ", numberOfWords)
print("\nNumber of chars: ", numberOfChars)
print("\nFrequencys of words", wordFrequency)
print("\nSorted Frequencies of words", sortedFrequencies)

