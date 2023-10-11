from mrjob.job import MRJob
from mrjob.step import MRStep

class UserReviewCount(MRJob):

    def steps(self):
        return [
            MRStep(mapper=self.mapper, reducer=self.reducer)
        ]

    def mapper(self, _, line):
        userId, movieId, _, _ = line.split(',')
        yield userId, 1

    def reducer(self, userId, counts):
        yield userId, sum(counts)

if name == 'main':
    # Here you can provide the hardcoded input file name
    inputFile = 'path_to_input_file.txt'
    
    # Running the job with the specified input
    UserReviewCount(args=[inputFile]).run()