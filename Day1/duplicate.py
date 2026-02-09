
from typing import List

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        return len(set(nums)) != len(nums)

testcases = [
    ([1, 2, 3, 4], False),
    ([1, 2, 3, 2], True),
    ([], False),
    ([42], False),
    ([5, 5, 5, 5], True),
    ([-1, -2, -3, -1], True),
    (list(range(1000)), False),
    (list(range(1000)) + [500], True)
]

if __name__ == "__main__":
    all_ok = True
    for i, (nums, expected) in enumerate(testcases):
        result = Solution().hasDuplicate(nums)
        ok = (result == expected)
        print(f"Test {i}: result={result}, expected={expected} -> {'PASS' if ok else 'FAIL'}")
        all_ok = all_ok and ok
    if not all_ok:
        raise SystemExit("Some tests failed")
    else:
        print("All tests passed")

for i, (nums, expected) in enumerate(testcases):
    def test_case():
        assert Solution().hasDuplicate(nums) is expected
    test_case.__name__ = f"test_case_{i}"
    globals()[test_case.__name__] = test_case
