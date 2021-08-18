import copy

def press(lights, i, j):
    lights[i][j] = 1 - lights[i][j]

    if i - 1 >= 0:
        lights[i-1][j] = 1 - lights[i-1][j]

    if j - 1 >= 0:
        lights[i][j-1] = 1 - lights[i][j-1]

    if i + 1 < 10:
        lights[i+1][j] = 1 - lights[i+1][j]

    if j + 1 < 10:
        lights[i][j+1] = 1 - lights[i][j+1]

def main():
    lights = []
    ans = 99999999

    for _ in range(10):
        lights.append([0 if x == "#" else 1 for x in input()])

    for i in range(2**10):
        bit_i = bin(i).lstrip('0b').zfill(10)

        count = 0

        temp_lights = copy.deepcopy(lights)

        for j in range(10):
            if bit_i[j] == "1":
                press(temp_lights, 0, j)
                count += 1

        for j in range(1, 10):
            for k in range(10):
                if temp_lights[j-1][k] == 1:
                    press(temp_lights, j, k)
                    count += 1


        if sum(temp_lights[9]) == 0:
            ans = min(ans, count)


    if ans == 99999999:
        print(-1)

    else:
        print(ans)



main()