the_truth = "Knowledge is power"
print ( the_truth )
print ( the_truth.replace (' ','\n') )      #ersätter alla mellanslag med \n

split_truth = str.split(the_truth)      #alternativt sätt: splittar strängen
for i, word in enumerate(split_truth):      #itererar genom listan
    print(word)

truth_border = the_truth.center(30,' ')      #Lägger till space på kanterna
truth_border=f'▌{truth_border}▐'        #lägger till kanten
top_border = '▄'*len(truth_border)    #genererar en stäng som består av = med samma längd som truth_border
bottom_border = '▀'*len(truth_border)    #genererar en stäng som består av = med samma längd som truth_border
print(top_border)
print(truth_border)
print (bottom_border)
