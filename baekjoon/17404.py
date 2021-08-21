import sys
def main():
    N = int(input())
    BIG_INT = 9999999999
    price = [(0, 0, 0)]
    dpR = [{"R": BIG_INT, "G": BIG_INT, "B": BIG_INT} for _ in range(N+3)]
    dpG = [{"R": BIG_INT, "G": BIG_INT, "B": BIG_INT} for _ in range(N+3)]
    dpB = [{"R": BIG_INT, "G": BIG_INT, "B": BIG_INT} for _ in range(N+3)]
    for _ in range(N):
        price.append(list(map(int, sys.stdin.readline().strip().split())))

    dpR[1]["R"] = price[1][0]
    dpG[1]["G"] = price[1][1]
    dpB[1]["B"] = price[1][2]

    for i in range(2, N):
        # R
        dpR[i]["R"] = min(dpR[i-1]["G"], dpR[i-1]["B"]) + price[i][0]
        dpR[i]["G"] = min(dpR[i-1]["R"], dpR[i-1]["B"]) + price[i][1]
        dpR[i]["B"] = min(dpR[i-1]["R"], dpR[i-1]["G"]) + price[i][2]

        # G
        dpG[i]["R"] = min(dpG[i-1]["G"], dpG[i-1]["B"]) + price[i][0]
        dpG[i]["G"] = min(dpG[i-1]["R"], dpG[i-1]["B"]) + price[i][1]
        dpG[i]["B"] = min(dpG[i-1]["R"], dpG[i-1]["G"]) + price[i][2]

        # B
        dpB[i]["R"] = min(dpB[i-1]["G"], dpB[i-1]["B"]) + price[i][0]
        dpB[i]["G"] = min(dpB[i-1]["R"], dpB[i-1]["B"]) + price[i][1]
        dpB[i]["B"] = min(dpB[i-1]["R"], dpB[i-1]["G"]) + price[i][2]


    dpR[N]["G"] = min(dpR[N-1]["R"], dpR[N-1]["B"]) + price[N][1]
    dpR[N]["B"] = min(dpR[N-1]["R"], dpR[N-1]["G"]) + price[N][2]

    dpG[N]["R"] = min(dpG[N-1]["G"], dpG[N-1]["B"]) + price[N][0]
    dpG[N]["B"] = min(dpG[N-1]["R"], dpG[N-1]["G"]) + price[N][2]

    dpB[N]["R"] = min(dpB[N-1]["G"], dpB[N-1]["B"]) + price[N][0]
    dpB[N]["G"] = min(dpB[N-1]["R"], dpB[N-1]["B"]) + price[N][1]

    print(min(min(dpR[N].values()), min(dpG[N].values()), min(dpB[N].values())))

main()