# start


info: str = "Moshe Haim Levi from Ashdod"

print('len', len(info))      # SECTION A

print('upper', info.upper())    # SECTION B

print('upper', info.lower())    # SECTION C

print('start with Moshe', info.startswith('Moshe'))   # SECTION D

print('ends  with Ashdod', info.endswith('Ashdod'))   # SECTION E

split_list: list[str] = info.split()  # SECTION F

print('with stars:', split_list)

stars_moshe = info.replace(' ', '*') # SECTION G

print(info.replace(' ', '*'))
print(stars_moshe)

print(stars_moshe.center(50, '=')) # SECTION H

print(stars_moshe[4:]) # SECTION I

print(stars_moshe[:4])  # SECTION J

print(stars_moshe[::2]) # SECTION K

print(stars_moshe.title())  # SECTION L

# end


