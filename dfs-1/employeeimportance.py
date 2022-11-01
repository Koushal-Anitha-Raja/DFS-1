"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        self.mem = {}
        for emp in employees:
            self.mem[emp.id] = {
                "key": emp.importance,
                "value": emp.subordinates
            }
        def recur(id):
            curr = self.mem[id]["key"]
            for sub in self.mem[id]["value"]:
                curr += recur(sub)
            return curr
        return recur(id)
            