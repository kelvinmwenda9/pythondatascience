def lists_tuples():
    # below are tuples, elements are closed using ()
    counties = ('Nairobi','Kisumu','Meru','Laikipia','Nyeri','Kitui')
    population = (600000,850050,900005,588850,9889800)
    print(counties[3])
    print(population[4])

    # below are lists, elements are closed using []
    towns = ['Nairobi','kisumu','meru','nyeri','samburu']
    fare = [60,350,860,900,500,400]
    print(fare)
    print(towns)
    print(type(fare))
    print(type(population))

    # lists vs tuples

    # tuples cant be updated, they are static, no add/remove
    # can be updated, they are dynamic, can add/remove items

    for x in range(1,2):
        towns.remove('Nairobi')
        towns.append('moyale')
        towns.insert(0, 'Nakuru')

    print(towns)


lists_tuples()


def palendrome():
    word = 'modcom'
    reverse = word[::-1]
    print(word)
    print(reverse)

palendrome()