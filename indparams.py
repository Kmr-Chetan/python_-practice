def printargs(**kwargs):
    for k,v in kwargs.items():
        print("k was passed", v, "value")

def printargs2(sub=None, to=None, body= None):
    print(to, sub, body)

pd={"to":"abc@gmail.com","sub":"hello", "body":"meeting @5:00pm"}
# printargs(to="abc@gmail.com",sub="hello", body="meeting @5:00pm")
printargs2(pd)