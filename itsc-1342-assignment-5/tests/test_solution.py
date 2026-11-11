# [Everrett Nguyen] - Assignment 5 Unit Tests
import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'code')))
from solution import sanitize_ip_list

# Test 1: Single blocked IP removed and invalid IP converted
sample1 = ["192.168.1.1", "10.0.0.1", "invalid", "172.16.0.4"]
expected1 = ["192.168.1.1", "10.0.0.1", "0.0.0.0", "172.16.0.4"]
assert sanitize_ip_list(sample1, "10.0.0.99") == expected1, "Failed Test 1: Check sanitizing logic"

# Test 2: Consecutive duplicate blocked IPs
sample2 = ["10.0.0.1", "10.0.0.1", "192.168.1.50"]
expected2 = ["192.168.1.50"]
assert sanitize_ip_list(sample2, "10.0.0.1") == expected2, "Failed Test 2: Did all blocked entries get caught?"

# Test 3: Ensure original list is unchanged or matches expected result format
sample3 = ["10.0.0.5", "10.0.0.6"]
# Notice the test call below:
assert sanitize_ip_list(sample3, "10.0.0.5") == ["10.0.0.6"], "Failed Test 3"

print("ALL UNIT TESTS PASSED - ASSIGNMENT 5")