from coverage import Coverage
from bubbleSort import BubbleSort
def generateCoverage(func,X,y,outfile_name):
    file_list = []
    result_list = []
    for i in range(len(X)):
        try:
            cov = Coverage()
            cov.start()
            if(func(X[i])==y[i]):
                result_list.append(1)
            else:
                result_list.append(0)
            cov.stop()
            cov.save()
            cov.json_report(outfile=outfile_name+"_"+str(i)+".json")
            file_list.append(outfile_name+"_"+str(i)+".json")
        except ValueError:
            print("ValueError is happened")
    return file_list,result_list

if __name__ == '__main__':
    X = [[1,2,3,4,4,2]]
    y = [[1,2,2,3,4,4]]
    filelist,result_list = generateCoverage(BubbleSort,X,y,"bubbleSort111")
    print(result_list)
