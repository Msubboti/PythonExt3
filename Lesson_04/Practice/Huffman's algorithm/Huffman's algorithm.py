
f =open(r"D:\Python\TechTool1.log",'r')
Dictionary = dict()
for lines in f:
    a = str(lines)
    for item in a:
        if item in Dictionary:
            Dictionary[item] += 1
        else:
            Dictionary[item] = 1
f.close()

keys_dict = list(Dictionary.keys())
vales_dict = list()
for keys in range(0,len(keys_dict)-1):
    vales_dict.append(Dictionary[keys_dict[keys]])
sort_keys = list()
sort_values = list()

while keys_dict and vales_dict:
        index = vales_dict.index(max(vales_dict))
        sort_keys.append(keys_dict.pop(index))
        sort_values.append(vales_dict.pop(index))

sort_keys.append(keys_dict[0])
sort_values.append(Dictionary[keys_dict[0]])
binary = [bin(i) for i in range(0,len(sort_keys))]




coding = dict()
for temp_item in range(0,len(sort_values)):
    coding[sort_keys[temp_item]] = binary[temp_item]

read = open(r"D:\Python\TechTool1.log",'r')
output= open(r"D:\Python\Output.bin", 'wb')


for lines in read:
    l = list(lines)
    for item in l:

        output.write(str(int(coding[item], 2)).encode('U8') + ' '.encode('U8'))
read.close()
output.close()

decoding = open(r"D:\Python\Decoding.txt", 'w')
reading = open(r"D:\Python\Output.bin",'rb')
for line in reading:
    string = line.decode('utf-8').split(' ')
    for symbol in string:
        decoding.write(sort_keys[int(symbol)])

reading.close()
decoding.close()