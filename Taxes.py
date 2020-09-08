income = float(input('Vad tjänar du?'))
tak1 = 38000 #vet inte riktigt vad jag ska kalla dessa
tak2 = 50000
tax_index = 0.3
extra_tax = 0.05
tax=0


tax = income*tax_index

if income > tak1:
    over_tak1 = income - tak1
    tax = tax + over_tak1*extra_tax
    if income > tak2: #lägger den här. Behöver inte kolla detta om inkomsten är mindre än första taket 
        over_tak2 = income - tak2
        tax = tax + over_tak2*extra_tax

print(f'Din skatt är: {round(tax)}')
