fruit_color(apple, red).
fruit_color(banana, yellow).
fruit_color(grape, purple).
fruit_color(orange, orange).
fruit_color(lemon, yellow).
fruit_color(strawberry, red).
color_of_fruit(Fruit, Color) :-
    fruit_color(Fruit, Color).
