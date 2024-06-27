edge(a, b, 2).
edge(a, c, 5).
edge(b, d, 3).
edge(c, e, 4).
edge(d, g, 1).
edge(e, g, 7).

best_first_search(Start, Goal) :-
    empty_priority_queue(EmptyQueue),
    add_to_queue(Start, EmptyQueue, Queue),
    search(Goal, Queue).

search(Goal, Queue) :-
    remove_from_queue(Goal, Queue, _), % Goal found
    format('Goal ~w found.~n', [Goal]).

search(Goal, Queue) :-
    remove_from_queue(Node, Queue, RestQueue),
    findall(Child, edge(Node, Child, _), Children),
    add_list_to_queue(Children, RestQueue, NewQueue),
    search(Goal, NewQueue).
empty_priority_queue([]).

add_to_queue(Node, Queue, NewQueue) :-
    heuristic(Node, H),
    insert_queue(Node, H, Queue, NewQueue).

add_list_to_queue([], Queue, Queue).
add_list_to_queue([Node | RestNodes], Queue, NewQueue) :-
    add_to_queue(Node, Queue, TempQueue),
    add_list_to_queue(RestNodes, TempQueue, NewQueue).

remove_from_queue(Node, Queue, RestQueue) :-
    del_queue(Node, _, Queue, RestQueue).

insert_queue(Node, H, [], [(Node, H)]).

insert_queue(Node, H, [(Node2, H2) | RestQueue], [(Node, H), (Node2, H2) | RestQueue]) :-
    H =< H2.

insert_queue(Node, H, [(Node2, H2) | RestQueue], [(Node2, H2) | NewRestQueue]) :-
    H > H2,
    insert_queue(Node, H, RestQueue, NewRestQueue).

del_queue(First, First, [(First, H) | RestQueue], RestQueue).

del_queue(Element, First, [(Element2, H) | RestQueue], [(Element2, H) | NewRestQueue]) :-
    Element \= Element2,
    del_queue(Element, First, RestQueue, NewRestQueue).
empty_priority_queue([]).

add_to_queue(Node, Queue, NewQueue) :-
    heuristic(Node, H),
    insert_queue(Node, H, Queue, NewQueue).

add_list_to_queue([], Queue, Queue).
add_list_to_queue([Node | RestNodes], Queue, NewQueue) :-
    add_to_queue(Node, Queue, TempQueue),
    add_list_to_queue(RestNodes, TempQueue, NewQueue).

remove_from_queue(Node, Queue, RestQueue) :-
    del_queue(Node, _, Queue, RestQueue).

insert_queue(Node, H, [], [(Node, H)]).

insert_queue(Node, H, [(Node2, H2) | RestQueue], [(Node, H), (Node2, H2) | RestQueue]) :-
    H =< H2.

insert_queue(Node, H, [(Node2, H2) | RestQueue], [(Node2, H2) | NewRestQueue]) :-
    H > H2,
    insert_queue(Node, H, RestQueue, NewRestQueue).

del_queue(First, First, [(First, H) | RestQueue], RestQueue).

del_queue(Element, First, [(Element2, H) | RestQueue], [(Element2, H) | NewRestQueue]) :-
    Element \= Element2,
    del_queue(Element, First, RestQueue, NewRestQueue).
empty_priority_queue([]).

add_to_queue(Node, Queue, NewQueue) :-
    heuristic(Node, H),
    insert_queue(Node, H, Queue, NewQueue).

add_list_to_queue([], Queue, Queue).
add_list_to_queue([Node | RestNodes], Queue, NewQueue) :-
    add_to_queue(Node, Queue, TempQueue),
    add_list_to_queue(RestNodes, TempQueue, NewQueue).

remove_from_queue(Node, Queue, RestQueue) :-
    del_queue(Node, _, Queue, RestQueue).

insert_queue(Node, H, [], [(Node, H)]).

insert_queue(Node, H, [(Node2, H2) | RestQueue], [(Node, H), (Node2, H2) | RestQueue]) :-
    H =< H2.

insert_queue(Node, H, [(Node2, H2) | RestQueue], [(Node2, H2) | NewRestQueue]) :-
    H > H2,
    insert_queue(Node, H, RestQueue, NewRestQueue).

del_queue(First, First, [(First, H) | RestQueue], RestQueue).

del_queue(Element, First, [(Element2, H) | RestQueue], [(Element2, H) | NewRestQueue]) :-
    Element \= Element2,
    del_queue(Element, First, RestQueue, NewRestQueue).
empty_priority_queue([]).

add_to_queue(Node, Queue, NewQueue) :-
    heuristic(Node, H),
    insert_queue(Node, H, Queue, NewQueue).

add_list_to_queue([], Queue, Queue).
add_list_to_queue([Node | RestNodes], Queue, NewQueue) :-
    add_to_queue(Node, Queue, TempQueue),
    add_list_to_queue(RestNodes, TempQueue, NewQueue).

remove_from_queue(Node, Queue, RestQueue) :-
    del_queue(Node, _, Queue, RestQueue).

insert_queue(Node, H, [], [(Node, H)]).

insert_queue(Node, H, [(Node2, H2) | RestQueue], [(Node, H), (Node2, H2) | RestQueue]) :-
    H =< H2.

insert_queue(Node, H, [(Node2, H2) | RestQueue], [(Node2, H2) | NewRestQueue]) :-
    H > H2,
    insert_queue(Node, H, RestQueue, NewRestQueue).

del_queue(First, First, [(First, H) | RestQueue], RestQueue).

del_queue(Element, First, [(Element2, H) | RestQueue], [(Element2, H) | NewRestQueue]) :-
    Element \= Element2,
    del_queue(Element, First, RestQueue, NewRestQueue).
empty_priority_queue([]).

add_to_queue(Node, Queue, NewQueue) :-
    heuristic(Node, H),
    insert_queue(Node, H, Queue, NewQueue).

add_list_to_queue([], Queue, Queue).
add_list_to_queue([Node | RestNodes], Queue, NewQueue) :-
    add_to_queue(Node, Queue, TempQueue),
    add_list_to_queue(RestNodes, TempQueue, NewQueue).

remove_from_queue(Node, Queue, RestQueue) :-
    del_queue(Node, _, Queue, RestQueue).

insert_queue(Node, H, [], [(Node, H)]).

insert_queue(Node, H, [(Node2, H2) | RestQueue], [(Node, H), (Node2, H2) | RestQueue]) :-
    H =< H2.

insert_queue(Node, H, [(Node2, H2) | RestQueue], [(Node2, H2) | NewRestQueue]) :-
    H > H2,
    insert_queue(Node, H, RestQueue, NewRestQueue).

del_queue(First, First, [(First, H) | RestQueue], RestQueue).

del_queue(Element, First, [(Element2, H) | RestQueue], [(Element2, H) | NewRestQueue]) :-
    Element \= Element2,
    del_queue(Element, First, RestQueue, NewRestQueue).

