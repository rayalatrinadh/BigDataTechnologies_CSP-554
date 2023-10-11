from mrjob.job import MRJob

class MRSalaries2(MRJob):

    def mapper(self, _, line):
        (name, jobTitle, agencyID, agency, hireDate, annualSalary, grossPay) = line.split('\t')
        
        # Convert the annualSalary string to float
        salary = float(annualSalary.replace(",", "").replace("$", ""))
        
        # Categorize the salary range
        if salary >= 100000:
            yield "High", 1
        elif 50000 <= salary < 100000:
            yield "Medium", 1
        else:
            yield "Low", 1

    def combiner(self, salary_range, counts):
        yield salary_range, sum(counts)

    def reducer(self, salary_range, counts):
        yield salary_range, sum(counts)


if __name__ == '__main__':
    MRSalaries2.run()