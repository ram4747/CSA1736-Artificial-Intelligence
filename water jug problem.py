def pour_water():
    max_size_3 =3
    max_size_4 = 4
    jug_3 = 0
    jug_4 = 0
    jug_4 = min(max_size_4, jug_4 + (max_size_4 - jug_4))
    print(jug_4, jug_3)
    space_left_3 = max_size_3 - jug_3
    jug_3 += min(jug_4, space_left_3)
    jug_4 -= min(jug_4, space_left_3)
    print(jug_4, jug_3)
    jug_3 = 0
    print(jug_4, jug_3)
    jug_3 = min(max_size_3, jug_4 + jug_3)
    jug_4 -= jug_3
    print(jug_4, jug_3)
    jug_4 = min(max_size_4, jug_4 + (max_size_4 - jug_4))
    print(jug_4, jug_3)
    space_left_3 = max_size_3 - jug_3
    jug_3 += min(jug_4, space_left_3)
    jug_4 -= min(jug_4, space_left_3)
    print(jug_4, jug_3)
pour_water()
