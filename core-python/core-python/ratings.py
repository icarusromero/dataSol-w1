"""Restaurant rating lister."""


# put your code here
file = open('scores.txt', 'r')

rest_ratings = {}

for line in file:
    line_pair = line.split(':')
    rest_ratings[line_pair[0]] = line_pair[1]

def print_alph_order():
    for rating in sorted(rest_ratings):
        print(rating + ' is rated at ' + rest_ratings.get(rating))

print_alph_order()

new_rest_name = input('Add a resturuant to rate: ')
new_rest_rating = input('Rate resuruant: ')
rest_ratings[new_rest_name] = new_rest_rating

print_alph_order()

file.close()