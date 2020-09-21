#!/usr/bin/python3
my_foods = ['pizza', 'falafel', 'carrot cacke']
friend_foods = my_foods[:]
# Da forma abaixo a lista é a mesma, na verdade é como um alias
#friend_foods = my_foods

my_foods.append('cannoli')
friend_foods.append('ice cream')

print("Minha comida favorita é:")
print(my_foods)

print("\nA comida favorita do meu amigo é:")
print(friend_foods)
