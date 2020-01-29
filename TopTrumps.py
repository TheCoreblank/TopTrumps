import json, requests, datetime, sys

playerLOC = []
AILOC = []

def writelog(log):
     with open('logs.txt', 'a') as logs:
            date = str(datetime.datetime.now())
            print(type(date))
            logs.write(date + ': ' + log)

def getdata():
    data = requests.get("https://hats184.github.io/api/toptrumps/robot/robot.json")
    data = data.text
    #print(type(data), data)
    if data == 'Not Found':
        writelog('Unsucessfull json file finding. ')
        print('Sorry, but we cannot find the data. Look at logs.txt for more infomation. Now terminating application')
        sys.exit()
    else:
        pokemonDict = json.loads(data)
        return pokemonDict

for i in range(26):
    playerLOC.append(getdata()[str(i)])
    oi = i
    i += 1
    AILOC.append(getdata()[str(i)])
    i = oi

#print(playerLOC, AILOC)



