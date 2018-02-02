#testing fake in mailroom?

def foobar():
    prompt = getInput('1 or 2\r\n')
    if prompt == '1':
        return 10
    elif prompt == '2':
        return 20

def getInput(prompt):
    return input(prompt)

def fake1(prompt):
    return "1"

def fake2(prompt):
    return "2"

getInput = fake1
res = foobar()
print(res)

getInput = fake2
res = foobar()
print(res)