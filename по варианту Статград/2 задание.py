# (¬y → (z ≡ w)) ∧ ((z → x) ≡ w)
print('x y z w')
for x in (0, 1):
    for y in (0, 1):
        for z in (0, 1):
            for w in (0, 1):
                # print(x, y, z, w)
                if (y + (z==w))  * ( (z-x != 1) == w) == 1:
                    print(x, y, z, w)
