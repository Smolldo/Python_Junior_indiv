# age = 75
# # or - або, and - і, not - не
# if age < 18:
#     print('ви неповнолітній')
# elif age >= 18 and age  <= 65:
#     print('ви дорослий')
# else:
#     print('u r pensioner')

day1 = 'Friday'
day2 = 'Sunday'

# if day1 == 'Saturday' or day2 == 'Sunday':
    # print('WEEKEND')


answer = 'maybe'

if answer == 'yes':
    print('u answered yes')
elif answer == 'no':
    print('u answered no')
else:
    print('answer is not recognized')


import turtle

screen = turtle.Screen()
t = turtle.Turtle()

direction = input('Enter: left, right, forward, back: ')

if direction == 'left':
    t.left(90)
    t.forward(100)
elif direction == 'right':
    t.right(90)
    t.forward(100)

screen.mainloop()