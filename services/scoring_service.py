class ScoringService:

    def score(self, scholarship):

        score = 0

        if scholarship.country in [
            "Canada",
            "United Kingdom",
            "United States",
            "Australia",
            "New Zealand"
        ]:
            score += 15

        if scholarship.coverage == "Full":
            score += 30

        if scholarship.level == "Bachelor":
            score += 25

        if scholarship.colombians:
            score += 20

        if scholarship.age >= 16:
            score += 10

        return score
