from json import load

with open('input_person.json') as data:
	people=load(data)
	for person in people['people']:
		if person['age'] >= 30:
			print('Name: {}, City: {}'.format(person['name'],person['city']))
