from mrjob.job import MRJob
from mrjob.step import MRStep

class UserReviewCount(MRJob):

    def mapper(self, _, line):
        userId, movieId, _, _ = line.split(',')
        yield userId, 1

    def reducer(self, userId, counts):
        yield userId, sum(counts)

if __name__ == '__main__':
    UserReviewCount.run()
