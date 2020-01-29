import json, urllib.request, datetime, sys

playerLOC = []
AILOC = []

def writelog(log):
     with open('logs.txt', 'a') as logs:
            logs.write(datetime.datetime.now() + ': ' + log)

def getdata():
    data = urllib.request.urlopen("https:///hats184.github.io/api/toptrumps/robot/robot.json").readall()
    data = data.decode('UTF-8')
    if data == 'Not Found':
        print('Sorry, but we cannot find the data. Look at logs.txt for more infomation. Now terminating application')
        writelog('Terminated Application')
        sys.exit()
    else:
        pokemonDict = json.loads(data)
        writelog('Suceesfull loading of robot.json')
        return pokemonDict

for i in range(26):
    playerLOC.append(getdata()[i])
    oi = i
    i += 1
    AILOC.append(getdata([i]))
    i = oi

print(playerLOC, AILOC)



