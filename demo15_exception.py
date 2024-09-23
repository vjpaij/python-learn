def remainder_division(a,b):
    if a==0 and b==0:
        raise Exception("Numbers can't be zeroes")
    if b==0:
        raise ZeroDivisionError
    result = a//b
    remainder = a%b
    print(result, remainder)

acr_dict = {}
acr_dict['LOL'] = "laugh out loud"
acr_dict['IDK'] = "I don't know"
acr_dict['TGIF'] = "Thank God its Friday"
acr_dict['TBH'] = "to be honest"

try: 
    definition = acr_dict['LOL']
    print(definition)
except:
    print("Acronym not found")
finally:
    print("Shall run irrespective of error or not")

remainder_division(0,0)