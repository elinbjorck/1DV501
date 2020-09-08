time = [0,0,0] #[seconds, minutes, hours]
seconds = 0
print(len(time))
while True: #Fortsätter loopa tills man skrivit in ett heltal
    seconds = input('skriv in ett antal sekunder(heltal): ')
    try:
        seconds = int(seconds)
        break
    except ValueError as error:
        print(f'\n {error} är inte ett heltal.')
#kollar resten när man delar med 60 för sekunder. heltalsdivision med 60 ger minuter. gör samma operationer på minuter för att få fram timmar och minuter

time[0] = seconds%60
time[1] = seconds//60
time[2] = time[1]//60
time[1] = time[1]%60

print (f'timmar: {time[2]}')
print (f'minuter: {time[1]}')
print (f'sekunder: {time[0]}')


