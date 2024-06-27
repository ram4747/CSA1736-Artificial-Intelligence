at(monkey, door, s0).
at(banana, middle, s0).
at(box, window, s0).
on_floor(s0).

move(P, P, S, S).
move(P1, P2, S, S2) :-
    on_floor(S),
    at(monkey, P1, S),
    at(box, P2, S),
    S2 = S.

climb(s0, s1) :-
    on_floor(s0),
    at(monkey, P, s0),
    at(box, P, s0).

climb(S, S2) :-
    on_floor(S),
    at(monkey, P, S),
    at(box, P, S),
    S2 = S.

push(P1, P2, S, S2) :-
    on_floor(S),
    at(monkey, P1, S),
    at(box, P1, S),
    move(P1, P2, S, S2).

grasp(s2, s3) :-
    at(monkey, P, s2),
    at(banana, P, s2),
    on_floor(s2).

solve(S, []) :-
    at(banana, P, S),
    at(monkey, P, S),
    on_floor(S).

solve(S, [A | As]) :-
    A = climb(S, S2); A = grasp(S, S2); A = push(_, _, S, S2),
    solve(S2, As).
