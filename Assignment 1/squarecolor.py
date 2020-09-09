identifier = input('Enter a chess square identifyer (from a1 to h8)')
letter = identifier[0]
number = int(identifier[1]) #här i början kan man sätta in checkar för att kolla så att användaren skriver in en ruta som faktiskt finns på brädet. 

#skulle kunna lägga in och testa så att användaren skriver in det på rätt format

letter = letter.lower()  #ifall någon skulle skriva in versaler
print(letter)
letter_number = ord(letter)-ord('a')+1 # Will find the letters distance from a, will give numbers from 0 to 7, 
                                         #then we ad 1 to get numbers from 1 to 8

black = letter_number % 2 == number % 2 #skriver man om bokstäverna till siffror (a:h)->(1:8) ser man att på de svarta 
                                          #rutorna är tecknen på siffrorna samma. På de vita rutorna är tecknen olika

if black:
    print(f'{identifier} is black')
else:
    print(f'{identifier} is white')
