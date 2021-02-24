import requests
import json
newDict = dict()
loadDict = dict()

end = 0

url = 'http://www.floatrates.com/daily/USD.json'
response = requests.get(url)
json_data = json.loads(response.text)
newDict["EUR"] = json_data['eur']
loadDict["USD"] = [newDict]
newDict = dict()

url = 'http://www.floatrates.com/daily/USD.json'
response = requests.get(url)
json_data = json.loads(response.text)
newDict["ILS"] = json_data['ils']
loadDict["USD"].append(newDict)







newDict = dict()

url = 'http://www.floatrates.com/daily/EUR.json'
response = requests.get(url)
json_data = json.loads(response.text)
newDict["USD"] = json_data['usd']
loadDict["EUR"] = [newDict]


newDict = dict()

url = 'http://www.floatrates.com/daily/EUR.json'
response = requests.get(url)
json_data = json.loads(response.text)
newDict["ILS"] = json_data['ils']
loadDict["EUR"].append(newDict)



change_from = input()
change_from = change_from.upper()

while change_from:
    try:
        flag1 = 0
        flag = 0
        valid_key = 999
        change_to = input()
        if change_to == "":
            exit()
        change_to = change_to.upper()

        amount = input()
        newDict = dict()
        print("Checking the cache…")

        if change_from in loadDict:
            for i in range(len(loadDict[change_from])):
                if change_to in loadDict[change_from][i]:
                    valid_key = i
                    flag1 = 1
                else:
                    pass

            if valid_key != 999 and flag1 == 1:
                print("Oh! It is in the cache!")
                final_thing = loadDict[change_from][valid_key][change_to]['rate'] * int(amount)
                print(f'"You received {round(final_thing, 2)} {change_to}."')

        if change_to in loadDict:
            for i in range(len(loadDict[change_to])):
                if change_from in loadDict[change_to][i]:
                    valid_key = i
                    flag = 2
                else:
                    pass

            if valid_key != 999 and flag == 2 and flag1 != 1:
                print("Oh! It is in the cache!")
                final_thing = loadDict[change_to][valid_key][change_from]['inverseRate'] * int(amount)
                print(f'"You received {round(final_thing, 2)} {change_to}."')







        if valid_key == 999:
            print("Sorry, but it is not in the cache!")
            url = 'http://www.floatrates.com/daily/' + change_from + '.json'
            response = requests.get(url)
            json_data = json.loads(response.text)
            newDict[change_to] = json_data[change_to.lower()]
            if change_from in loadDict:
                loadDict[change_from].append(newDict)
            else:
                loadDict[change_from] = [newDict]
            i = 0
            for i in range(len(loadDict[change_from])):
                if change_to in loadDict[change_from][i]:
                    valid_key = i
            final_thing = loadDict[change_from][i][change_to]['rate'] * int(amount)
            print(f'"You received {round(final_thing, 2)} {change_to}."')
    except EOFError:
        break
