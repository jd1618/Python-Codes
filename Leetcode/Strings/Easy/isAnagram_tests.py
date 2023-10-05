import pytest # version 7.4.2
import time
from isAnagram import isAnagram

# Test true outcomes:
def test_isAnagram_true():
	assert isAnagram('dusty','study')==True
	assert isAnagram('night','thing')==True
	assert isAnagram('arc','car')==True

# Test false outcomes:
def test_isAnagram_false():
	assert isAnagram('dusty','rusty')=False
	assert isAnagram('real','complex')=False
	assert isAnagram('abc','abd')=False

# Test edge cases such as case sensitivity:
def test_isAnagram_case_sensitive():
	assert isAnagram('dusty','Study')==False
	assert isAnagram('ABC','cba')==False
	assert isAnagram(' ','  ')==False

# Test edge cases such as space sensitivity:
def test_isAnagram_space_sensitive():
	assert isAnagram('dusty','study ')==False
	assert isAnagram('dusty',' study')==False

if __name__ == "__main__":
    pytest.main()

# Test the time complexity of isAnagram:
def test_time_complexity():
    input_sizes=[10,100,1000,10000] # Varying input sizes
    max_time=1 # For linear time complexity

    for size in input_sizes:
        s='a'*size
        t='a'*size
        start=time.time()
        is_anagram=isAnagram(s,t)
        end=time.time()
        duration=end-start

        assert is_anagram is True # Ensure correctness for this specific test case
        assert duration<=max_time*size # Linear time complexity

if __name__=="__main__":
    test_time_complexity()