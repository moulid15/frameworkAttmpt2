import os
import json

def Liner(path,arr,count):
    directory = os.fsencode(path)
    for file in os.listdir(directory):
        
        filename = os.fsdecode(file)
        try:
            with open(path+'\\'+str(filename)) as reader:
                for line in reader.readlines():
                    count.add(line)
                    if "\"OptOut\":\"ALL\"" in str(line):
                        
                        js = json.loads(line)
                        
                        arr.add(str(json.dumps(js['endpoint'], indent=4)))
                        #print(json.dumps(js['endpoint'], indent=4))

                #print("file: ", reader.readlines()[0])
        except:
            print(filename)
    

paths= ["C:\\Users\\moulidah\\Downloads\\cx\\Kinesis\\2022\\04\\05\\00","C:\\Users\\moulidah\\Downloads\\cx\\Kinesis\\2022\\04\\05\\01","C:\\Users\\moulidah\\Downloads\\cx\\Kinesis\\2022\\04\\05\\02","C:\\Users\\moulidah\\Downloads\\cx\\Kinesis\\2022\\04\\05\\03","C:\\Users\\moulidah\\Downloads\\cx\\Kinesis\\2022\\04\\05\\04","C:\\Users\\moulidah\\Downloads\\cx\\Kinesis\\2022\\04\\05\\05","C:\\Users\\moulidah\\Downloads\\cx\\Kinesis\\2022\\04\\05\\06","C:\\Users\\moulidah\\Downloads\\cx\\Kinesis\\2022\\04\\05\\07", "C:\\Users\\moulidah\\Downloads\\cx\\Kinesis\\2022\\04\\05\\08"]
arr = set()
count = set()
for path in paths:
    Liner(path,arr,count)
print("count: ", len(count))
#print(arr)
obj = ',\n'.join(list(arr))
obj = '['+obj +']'
#with open('json_data.json', 'w') as outfile:
    #outfile.write(obj)
    #outfile.close()
print(len(arr))