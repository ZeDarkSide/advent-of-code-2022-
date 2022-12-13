x, signals, crt = 1, 0, ""
for runs, ins in enumerate(open('input.txt').read().split(), start=1):
    signals += runs * x if runs % 40 == 20 else 0 
    crt += "\u2593" if (runs - 1) % 40 - x in (-1, 0 ,1) else "\u2591"
     #if not true to statment black space if true white space

    #this is for the first part of getting the numbers
    if ins[-1].isdigit(): 
        x += int(ins)
print(signals)
for i in range(0, len(crt), 40):
    print(crt[i: i +40])
