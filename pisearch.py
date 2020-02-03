import requests

s= 0;c=""
st="boo" ## add the search term here
while(not st in c):
    print("Running " + str(s), end=' ')
    parameters = {
        "numberOfDigits":1000,
        "start": s
    }
    response = requests.get("http://api.pi.delivery/v1/pi",params=parameters)
    x = 0;c = ""
    while x<1000:
        a = int(str(response.json()['content'])[x:x+2])%26
        c=c+chr(a+97)
        x=x+1
    s=s+1000
print()
print("found on: "+str(s+c.find(st)))
print(c[:c.find(st)]+'\033[95m'+'\033[1m'+c[c.find(st):c.find(st)+len(st)]+'\033[0m'+c[c.find(st)+len(st):])