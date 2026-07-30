class DeduplicationService:

    def remove_duplicates(self, scholarships):

        urls = set()

        unique = []

        for scholarship in scholarships:

            if scholarship.url not in urls:

                urls.add(scholarship.url)

                unique.append(scholarship)

        return unique
