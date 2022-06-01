
import json

ip_json = {"x":{"y":{"z":"b"}}}

ip_key_seq = "x/y/z"
 



def getValue(jsonObject , key):
    full_json = jsonObject
    key_seq_arr = key.split("/")
    for i in range(len(key_seq_arr)):
        if key_seq_arr[i] in full_json:
            full_json = full_json[key_seq_arr[i]]
            if i == (len(key_seq_arr) - 1):
                print('value = '+str(full_json)) 
                break
        else:
            print("Incorrect sequence provided")
            break
            
getValue(ip_json,ip_key_seq)