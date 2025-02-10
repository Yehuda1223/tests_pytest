def test_addition():
    assert 1 + 1 == 2

def test_fail():
    assert 2 + 25 == 5  

def ninus_one():
    assert 1 - 1 == 0
    
def test_subtraction():
    assert 1 - 1 == 0
    
    
def printt(text):
    print(text)
    
def test_printt():
    assert printt("Hello") == None
    
def test_printt2():
    assert printt("Hello") == None