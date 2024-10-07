import shioaji as sj

def hello() -> None:
    print("Hello from sj-trading!")

def get_shioaji_client() -> sj.Shioaji:
    api =  sj.Shioaji()
    print("Shioaji API created")
    return api
