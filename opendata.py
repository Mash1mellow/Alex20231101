import requests, json

url ="https://datacenter.taichung.gov.tw/swagger/OpenData/db36e286-1d2b-4784-99b9-3b0790dd9652"
Data = requests.get(url)
#print(Data.text)
JsonData = json.loads(Data.text)
#for x in JsonData:
	#print(x)
	#print()
Result = ""
for item in JsonData:
	Result += item["路口名稱"] + "：發生" + item["總件數"]+ "件，主因是" + item["主要肇因"] + "\n\n"
print(Result)
