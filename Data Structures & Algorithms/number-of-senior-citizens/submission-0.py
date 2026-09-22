class Solution:
    def countSeniors(self, details: List[str]) -> int:
        seniors = 0
        for passenger in details:
            age = int(passenger[11]) * 10 + int(passenger[12])

            if age > 60:
                seniors += 1

        return seniors