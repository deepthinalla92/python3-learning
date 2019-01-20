
import wget

def convert_file_to_array(file_url):
    file_path = '/Users/deepthinalla/Desktop/sample-data/sample-csv.csv'
    wget.download(file_url,file_path)
    with open(file_path,'r') as sample_data_file:
        data_lines = sample_data_file.readlines()
        keys = ['c1','c2','c3','c4']
        responseList = []
        for line in data_lines:
            responseDict = {}
            line = line.rstrip('\n')
            current_line = line.split(',')
            for column in current_line:
                for key in keys:
                    if key not in responseDict.keys():
                        responseDict[key] = column
                        break
            responseList.append(responseDict)
        print(responseList)
    return responseList

convert_file_to_array("https://raw.githubusercontent.com/binarybutter/assignments-input-files/master/csv-sample-data.csv")
