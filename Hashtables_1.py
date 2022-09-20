def getindex(a_string,data_list):
    result=0

    for ch in a_string :
        num=ord(ch)
        result+=num

    return result%len(data_list)

MAX_HASH_TABLE_SIZE = 4096
data_list=[None]*MAX_HASH_TABLE_SIZE
print(getindex('Aakash',data_list))


def get_valid_index(data_list,key):
    idx=getindex(key,data_list)

    while True:
        kv=data_list[idx]

        if kv is None:
            return idx

        k,v =kv
        if k==key:
            return idx

        idx+=1

        if idx==len(data_list):
            idx=0
            

class ProbingHashTable:
    def __init__(self,max_size=MAX_HASH_TABLE_SIZE):
        self.data_list=[None]*max_size

    def insert(self,key,value):
          idx=get_valid_index(self.data_list,key)
          self.data_list[idx]=(key, value)
         

    def find(self,key):
         idx=get_valid_index(self.data_list,key)
         kv=data_list[idx]
         return None if kv is None else kv[1]

    def update(self,key,value):
        idx=get_valid_index(self.data_list,key)
        self.data_list[idx]=key,value

    def list_all(self):
        return [kv[0] for kv in self.data_list if kv is not None]

probing_table = ProbingHashTable()
probing_table.insert('listen', 99)
print(probing_table.find('listen'))


