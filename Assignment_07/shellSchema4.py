foodratings_ex4 = foodratings.filter((foodratings['name'] == "Mel") & (foodratings['food3'] < 25))
foodratings_ex4.printSchema()
foodratings_ex4.show(5)