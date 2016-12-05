__author__ = "shikun"
import pickle
import os
from common import operateFile
from common.variable import GetVariable

def write_pickle(dict_data, path="data.pickle"):
    read = read_pickle(path)
    result = []
    if len(read) > 0:
        read.append(dict_data)
        result = read
    else:
        result.append(dict_data)
    with open(path, 'wb') as f:
        print(result)
        pickle.dump(result, f, 0)

def read_pickle(path):
    data = {}
    if operateFile.OperateFile(path).check_file():
        with open(path, 'rb') as f:
            try:
                data = pickle.load(f)
            except EOFError:
                pass
    print(data)
    return data
if __name__=="__main__":
    data = {"log":"132"}
    write_pickle(data, path=GetVariable.CRASH_LOG_PATH)
    read_pickle(path=GetVariable.CRASH_LOG_PATH)
    # operateFile.OperateFile(PATH("data.pickle")).remove_file()



