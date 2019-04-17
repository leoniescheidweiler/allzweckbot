import requests

def allesdreck():
    response = requests.get('http://rolf-schneider.net/mensa/')
    content = response.content.decode('utf-8').split('\n')

    #with open('example', 'w') as file:
        #file.write(content)

    #with open('example', 'r') as file:
        #content = file.readlines()

    meals_d = []
    next_d = False
    for line in content:
        line = line.strip('\n')
        if next_d and 'meal' in line:
            meals_d.append(line.split('>')[1].split('<')[0].split(','))
            next_d = False
        if 'maind' in line:
            next_d = True

    meals_e = []
    next_e = False
    for line in content:
        line = line.strip('\n')
        if next_e and 'meal' in line:
            meals_e.append(line.split('>')[1].split('<')[0].split(','))
            next_e = False
        if 'maine' in line:
            next_e = True

    forbidden_snacks = ['Tagessuppe', 'Salat der Saison']

    output = '```'
    output += 'Speisekarte INF 304\n\n'
    output += 'Aufgang D\n'
    for meal in meals_d:
        meal = [x.strip() for x in meal]
        meal = [item for item in meal if item not in forbidden_snacks]
        output+=('- '+', '.join(meal)+'\n')
    output += '\n'
    output += 'Aufgang E\n'
    for meal in meals_e:
        meal = [x.strip() for x in meal]
        meal = [item for item in meal if item not in forbidden_snacks]
        output+=('- '+', '.join(meal)+'\n')
    output += '```'
    return output
