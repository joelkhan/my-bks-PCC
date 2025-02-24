def show_magicians(magicians):
    for m in magicians:
        print(m)

def make_great(magicians):
    for i in range(len(magicians)):
        magicians[i] = 'the Great ' + magicians[i]
    return magicians

ourMagicians = ['小刘', '小张', '小李', '老王']
show_magicians(ourMagicians)
ourGreaters = make_great(ourMagicians[:])
show_magicians(ourGreaters)
