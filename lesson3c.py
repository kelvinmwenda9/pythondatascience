counties = ['Kisumu','Meru','Nairobi','Narok','Mombasa']
print(counties)

for county in counties:
    print(county)
    if county == 'Narok':
        break
    else:
        continue
