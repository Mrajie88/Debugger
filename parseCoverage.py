import json
def ParseCoverage(funcName,fileName):
    result = []
    lines = []
    for i in range(len(fileName)):
        temp = []
        with open(fileName[i],'r') as f:
            data = json.load(f)
            executed_lines = data["files"][funcName]["executed_lines"]
            missing_lines = data["files"][funcName]["missing_lines"]
            if(lines==[]):
                lines = executed_lines+missing_lines
                lines.sort()
            temp1= 0
            temp2= 0
            for i in range(len(executed_lines)+len(missing_lines)):
                if(temp1>=len(executed_lines)):
                    temp.append(0)
                    temp2+=1
                    continue
                if (temp2 >= len(missing_lines)):
                    temp.append(1)
                    temp1 += 1
                    continue
                if(executed_lines[temp1]<missing_lines[temp2]):
                    temp.append(1)
                    temp1+=1
                else:
                    temp.append(0)
                    temp2+=1
        result.append(temp)
    return result,lines

if __name__ == '__main__':
    fileName = "coverage.json"
    print(ParseCoverage(fileName))