import pandas

cols = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i','j', 'k']
df = pandas.read_csv('onehot2.csv', names = cols)
c = 0

for i in range(0, len(df)):
    c+=1
    print(c)
    if df['a'][i] == 1:
        df['k'][i] = 'HTC-1-M7'
    elif df['b'][i] == 1:
        df['k'][i] = 'LG-Nexus-5x'
    elif df['c'][i] == 1:
        df['k'][i] = 'iPhone-4s'
    elif df['d'][i] == 1:
        df['k'][i] = 'Motorola-Nexus-6'
    elif df['e'][i] == 1:
        df['k'][i] == 'Motorola-Droid-Maxx'
    elif df['f'][i] == 1:
        df['k'][i] == 'iPhone-6'
    elif df['g'][i] == 1:
        df['k'][i] == 'Sony-NEX-7'
    elif df['h'][i] == 1:
        df['k'][i] == 'Samsung-Galaxy-Note3'
    elif df['i'][i] == 1:
        df['k'][i] == 'Motorola-X'
    elif df['j'][i] == 1:
        df['k'][i] == 'Samsung-Galaxy-S4'

for i in range(0, len(df)):
    c +=1
    print(c)
    for j in range(0,10):
        if df['a'][j] == 1:
            df['k'][i] = 'HTC-1-M7'
            break
        elif df['b'][j] == 1:
            df['k'][i] = 'LG-Nexus-5x'
            break
        elif df['c'][j] == 1:
            df['k'][i] = 'iPhone-4s'
            break
        elif df['d'][j] == 1:
            df['k'][i] = 'Motorola-Nexus-6'
            break
        elif df['e'][j] == 1:
            df['k'][i] == 'Motorola-Droid-Maxx'
            break
        elif df['f'][j] == 1:
            df['k'][i] == 'iPhone-6'
            break
        elif df['g'][j] == 1:
            df['k'][i] == 'Sony-NEX-7'
            break
        elif df['h'][j] == 1:
            df['k'][i] == 'Samsung-Galaxy-Note3'
            break
        elif df['i'][j] == 1:
            df['k'][i] == 'Motorola-X'
            break
        elif df['j'][j] == 1:
            df['k'][i] == 'Samsung-Galaxy-S4'
            break
        break

df.to_csv('onehot3.csv', index=False, header=False)