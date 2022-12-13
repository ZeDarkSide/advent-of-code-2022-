#UP Down Left Right moves 
dirs = {"U": 1j,"D": -1j,"L":-1,"R":1} 
sigh = lambda a: (a>0) - (a < 0)
 # well this is the rope/string tracking the number
rope, s1,s2 = [0] *10, {0}, {0}
for lin in open('input.txt').read().splitlines(): 
    d, s = lin.split()

    for _ in range(int(s)):
        #makes the rope for the numbers
        rope[0] += dirs[d]
        for i in range(1, len(rope)):
            if abs(diff := rope[i -1] - rope[i]) >= 2:
                rope[i] += complex(sigh(diff.real), sigh(diff.imag))
        s2.add(rope[-1])
        s1.add(rope[1])
print(len(s1)) 
print(len(s2)) 
