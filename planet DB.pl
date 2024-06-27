planet(mercury, rocky, 0.39).
planet(venus, rocky, 0.72).
planet(earth, rocky, 1.00).
planet(mars, rocky, 1.52).
planet(jupiter, gas_giant, 5.20).
planet(saturn, gas_giant, 9.58).
planet(uranus, gas_giant, 19.22).
planet(neptune, gas_giant, 30.05).

planets_of_type(Type, Planets) :-
    findall(Name, planet(Name, Type, _), Planets).

