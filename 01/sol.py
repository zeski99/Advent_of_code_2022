print((lambda x: (x[-1], sum(x[-3:])))(sorted(sum(map(int, h.split())) for h in open("in.txt").read().split("\n\n"))))