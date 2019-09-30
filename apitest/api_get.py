import requests

def main():
    res = requests.get("http://5b74423ea5837400141908c3.mockapi.io/Demo")
    if res.status_code != 200:
        raise Exception("ERROR")
    for i in res.json():
        id = i["id"]
        name = i["name"]
        print(f"ID:{id} is Mr./Mrs. {name}")
if __name__ =="__main__":
    main()