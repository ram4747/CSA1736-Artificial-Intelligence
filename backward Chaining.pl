fact(has_fur, dog).
fact(has_tail, dog).
fact(has_fur, cat).
fact(has_tail, cat).
fact(has_feathers, bird).
rule(mammal, X) :-
    fact(has_fur, X),
    fact(has_tail, X).
rule(animals, X) :-
    fact(has_fur, X).
rule(animals, X) :-
    fact(has_feathers, X).

entails(Goal, _) :- fact(Goal, _).
entails(Goal, Derived) :-
    rule(Consequent, Goal),
    \+ member(Consequent, Derived), % Check if not already derived
    entails(Consequent, [Goal | Derived]).
prove(Goal) :-
    entails(Goal, []),
    write('Goal '), write(Goal), write(' is proved.'), nl.

prove(Goal) :-
    \+ entails(Goal, []),
    write('Goal '), write(Goal), write(' cannot be proved.'), nl.
