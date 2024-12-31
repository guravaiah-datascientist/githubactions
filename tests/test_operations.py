from src.maths_operations import add,sub

def test_add():
	assert add(2,3)==5
	assert add(4,6)==10
	assert add(7,8)==15

def test_sub():
	assert sub(3,6)==-3
	assert sub(6,3)==3
	assert sub(9,9)==0