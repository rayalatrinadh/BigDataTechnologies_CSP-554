ex6 = foodratings.join(foodplaces, foodratings.placeid == foodplaces.placeid, 'inner')
ex6.printSchema()
ex6.show(5)