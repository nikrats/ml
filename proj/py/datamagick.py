# Python3 code to demonstrate working of
# Extract substrings between brackets
# Using regex
# see: https://www.geeksforgeeks.org/python-extract-substrings-between-brackets/
import re

def get_ScaledData(path, startdataset, maxdataset):
    datasetVectors = []
    img_number = 0
    dataset_number = startdataset
    relpath = path
    while dataset_number <= maxdataset:
        img_number = 0
        while img_number <= 9:
            feature_vector = []
            print(str(dataset_number) + " " + str(img_number))
            try:
                with open(f"{relpath}/scaled{img_number}_{dataset_number}.txt", 'r') as f:
                    lines = f.readlines() # list containing lines of file
                    i = 1
                    for line in lines:
                        line = line.strip() # remove leading/trailing white spaces
                        if line:
                            if i == 1: # skip headline
                                i = i + 1
                            else:
                                res = re.findall(r'\(.*?\)', line)
                                #print(str(res[0]))
                                grayValStr = res[0]
                                grayValDigits = grayValStr[1:-1]
                                grayVal = grayValDigits.split(",")
                                feature_vector.append(int(grayVal[-1]))

                feature_vector.append(int(img_number))
                print(str(feature_vector))
                datasetVectors.append(feature_vector)
            except:
                print("file not found: " +str(dataset_number) + " " + str(img_number))
            img_number += 1
        dataset_number += 1

    print("Feature Vector : " + str(datasetVectors))
    return datasetVectors
