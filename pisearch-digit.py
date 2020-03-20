from concurrent.futures import ThreadPoolExecutor as PoolExecutor
import grequests

s=""
st="8146974"
def get_it(url):
    p=""
    rs = (grequests.get(u) for u in url)
    for i in grequests.map(rs):
        p=p+str(i.json()['content'])
    return p
    
start=0
upper=100000000
l=0

urls = ["http://api.pi.delivery/v1/pi?start="+str(x)+"&numberOfDigits=1000" for x in range(start,upper,1000)]
n=15
final = [urls[i * n:(i + 1) * n] for i in range((len(urls) + n - 1) // n )]  
with PoolExecutor(max_workers=8) as executor:
    for _ in executor.map(get_it, final):
        s=s+_
        p=len(s)
        if st in s:
            print("Found at:",s.find(st)+l)
            executor.shutdown(wait=False)
            break
        elif len(s)>100000:
            l=l+p
            s=""
        elif len(s)>=upper+start:
            print("not found at all")
        else:
            print("Not found: ",start+p+l) 
