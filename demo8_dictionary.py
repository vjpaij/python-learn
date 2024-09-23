acr_dict = {}
acr_dict['LOL'] = "laugh out loud"
acr_dict['IDK'] = "I don't know"
acr_dict['TGIF'] = "Thank God its Friday"
acr_dict['TBH'] = "to be honest"


print(acr_dict['IDK'])

abbr = acr_dict.get('BTW')
print(abbr)

for acr in acr_dict:
    print(acr)

for trans in acr_dict:
    print(acr_dict.get(trans))

sentence = "IDK" + " what happened " + "TBH"
translate = acr_dict.get('IDK') + " what happened " + acr_dict.get('TBH') 

print('sentence : ', sentence)
print('translate : ', translate)
