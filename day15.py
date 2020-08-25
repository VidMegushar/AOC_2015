
frost = [4,-2,0,0,5]
candy = [0,5,-1,0,8]
butt = [-1,0,5,0,6]
sugar = [0,0,-2,2,1]

best_score = 0
best_config = None
for f in range(101):
    for c in range(101 - f):
        for b in range(101 - f - c):
            for s in range(101 - f - c - b):
                if f+c+b+s == 100:
                    cap = f*frost[0] + c*candy[0] + b*butt[0] + s*sugar[0]
                    dur = f*frost[1] + c*candy[1] + b*butt[1] + s*sugar[1]
                    flav = f*frost[2] + c*candy[2] + b*butt[2] + s*sugar[2]
                    texture = f*frost[3] + c*candy[3] + b*butt[3] + s*sugar[3]
                    calories = f*frost[4] + c*candy[4] + b*butt[4] + s*sugar[4]

                    if cap < 0 or dur < 0 or flav < 0 or texture < 0:
                        tmp_score = 0
                    elif calories != 500:
                        tmp_score = 0
                    else:
                        tmp_score = cap*dur*flav*texture
                    if tmp_score > best_score:
                        best_score = tmp_score
"""

butt = [-1, -2, 6, 3, 8]
cinn = [2, 3, -2, -1, 3]


best_score = 0
best_config = None
for b in range(101):
    c = 100 - b
    cap = b*butt[0] + c*cinn[0]
    dur = b*butt[1] + c*cinn[1]
    flav = b*butt[2] + c*cinn[2]
    texture = b*butt[3] + c*cinn[3]
    if cap < 0 or dur < 0 or flav < 0 or texture < 0:
        tmp_score = 0
    else:
        tmp_score = cap*dur*flav*texture
    if tmp_score > best_score:
        best_score = tmp_score
        best_config = [b,c]
"""
print(best_score)