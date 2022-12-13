x, signals, crt = 1, 0, ""
for cycle, ins in enumerate(open('input.txt').read().split(), start=1):
    signals += cycle * x if cycle % 40 == 20 else 0 
    crt += "\u2593" if (cycle - 1) % 40 - x in (-1, 0 ,1) else "\u2591"
     #if not true to statment black space if true white space

    #this is for the first part of getting the numbers
    if ins[-1].isdigit(): 
        x += int(ins)
print(signals)
for i in range(0, len(crt), 40):
    print(crt[i: i +40])
