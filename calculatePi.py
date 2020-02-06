import random


# Adva van egy egységnyi sugarú kör, számold ki a pi-t, a lehető legnagyobb pontossággal.
# háromszög területe: (pi)r^2, a négyzeté pedig (2*r)^2 => pi/4 = a pontok a koron belül/pontok a körön kívül

# n - hány pontot használjon fel viszonyításul
def randompi(n):
    pontok_koron_belul = 0
    pontok_koron_kivul = 0

    for _ in range(n):
        pont_x = random.uniform(0, 1)
        pont_y = random.uniform(0, 1)

        if (pont_x**2 + pont_y**2)**0.5 <= 1:
            pontok_koron_belul += 1

        pontok_koron_kivul += 1

    return 4 * pontok_koron_belul / pontok_koron_kivul


print(randompi(100000))
