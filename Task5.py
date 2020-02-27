import requests

url = "http://172.17.50.43/freebix"
r = requests.get(url)
print("Status code:\n ******")
print(r.status_code)
print("OK")
h = requests.head(url)
print("Header:\n******")
for line in h.headers:
    print(line,":",h.headers[line])
    print("******")

ur12 = "http://172.17.50.43/headers.php"
fake_headers ={
    'User-Agent':'Mobile'
}
r2 = requests.get(ur12,headers = fake_headers)
print(r2.text)