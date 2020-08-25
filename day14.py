with open("input14.txt") as f:
    data = f.readlines()

class Reindeer():

    def __init__(self, speed, fly_time, rest_time):
        self.speed = speed
        self.fly_time = fly_time
        self.rest_time = rest_time
        self.distance_travelled = 0
        self.resting = False
        self.tmp_fly_time = fly_time
        self.tmp_rest_time = 0
        self.score = 0

    def move_one_sec(self):
        if not self.resting:
            self.distance_travelled += self.speed
            self.tmp_fly_time -= 1
            if self.tmp_fly_time == 0:
                self.tmp_rest_time = self.rest_time
                self.resting = True
        else:
            self.tmp_rest_time -= 1
            if self.tmp_rest_time == 0:
                self.tmp_fly_time = self.fly_time
                self.resting = False

TIME = 2503
def dist_travelled(speed, fly_time, rest_time, time):
    dist = 0
    while time > fly_time:
        dist += speed*fly_time
        time -= (fly_time + rest_time)
    if time > 0:
        dist += time*speed
    return dist

reindeers = []
for row in data:
    row = row.strip().split(" ")
    name = row[0]
    speed = int(row[3])
    fly_time = int(row[6])
    rest_time = int(row[-2])
    reindeers.append(Reindeer(speed, fly_time, rest_time))

rein_scores = [0 for _ in range(len(reindeers))]
for _ in range(TIME):
    for rein in reindeers:
        rein.move_one_sec()
    tmp_distances = [r.distance_travelled for r in reindeers]
    top_scorers = [i for i in range(len(reindeers)) if reindeers[i].distance_travelled == max(tmp_distances)]
    for i in top_scorers:
        rein_scores[i] += 1

print(max(rein_scores))

