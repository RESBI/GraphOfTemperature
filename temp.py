import time

tPoint = "="

tempGraph = [[" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "]
            ,[" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "]
            ,[" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "]
            ,[" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "]
            ,[" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "]
            ,[" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "]
            ,[" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "]
            ,[" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "]
            ,[" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "]
            ,[" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "]
            ,[" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "]
            ,[" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "]
            ,[" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "]
            ,[" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "]
            ,[" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "]
            ,[" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "]
            ,[" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "]
            ,[" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "]
            ,[" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "]
            ,[" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "]
            ,[" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "]
            ,[" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "]
            ,[" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "]
            ,[" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "]
            ,[" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "]
            ,[" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "]
            ,[" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "]
            ,[" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "]
            ,[" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "]
            ,[" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "]
            ,[" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "]
            ,[" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "]
            ,[0,5,10,15,20,25,30,35,40,45,50,55,60,65,70,75,80,85,90,95]]

while 1:
    print("\x1b[0;0H")
    temp = open("/sys/class/thermal/thermal_zone0/temp","r")
    tempT = temp.read().split("\n")[0]

    for i in range(len(tempGraph) - 2):
        tempGraph[i] = tempGraph[i + 1]

    tempGraph[-2] = [" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "]
    tempGraph[-2][int(int(tempT) / 5)] = tPoint

    for a in range(20):
        tempGra = ""
        for b in range(32):
            tempGra = tempGra + " "  + tempGraph[b][19 - a]
        print(tempGra + " -- " + str(tempGraph[-1][19 - a]))

    print("%s %s" % (tempT,time.time()))
#    print(temp.read())
    temp.close()
    time.sleep(1)
