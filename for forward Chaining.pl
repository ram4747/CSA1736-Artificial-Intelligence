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
derived([]).

forward_chaining :-
    derived(Derived),
    rule(Consequent, X),
    \+ member(Consequent, Derived), % Check if already derived
    \+ fact(Consequent, X), % Check if not already known as a fact
    (   check_conditions(X, Consequent) ->
        write('Derived: '), write(Consequent), write(' for '), write(X), nl,
        asserta(fact(Consequent, X)),
        append([Consequent], Derived, NewDerived),
        retract(derived(Derived)),
        asserta(derived(NewDerived))
    ;   true
    ),
        forward_chaining.
check_conditions(X, X). % Base case
check_conditions(X, Condition) :-
    rule(Condition, X),
    fact(Condition, X),
    check_conditions(X, Consequent).
