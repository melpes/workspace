from sys import stdin

while True:
    try:
        Rk, Rx, l1, v1 = map(float, stdin.readline().split(','))
        l2, v2 = map(float, stdin.readline().split(','))
        answer = (Rk * l2 / l1, Rk * v2 / v1)

        with open("report.txt", "a") as f:
            f.write("{:.2f}".format(answer[0]))
            f.write("\t")
            f.write("{:.2f}".format(answer[1]))
            f.write("\t")
            f.write("{:.2f}".format((Rx-answer[0]) / Rx * 100))
            f.write("\t")
            f.write("{:.2f}".format((Rx-answer[1]) / Rx * 100))
            f.write("\n")

    except:
        print("종료")
        break