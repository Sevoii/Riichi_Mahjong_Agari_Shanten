def calc_norm(fu, han, oya):
    if oya:
        match (fu, han):
            case (20, 2) | (40, 1):
                return (2000, 700, 0)
            case (20, 3) | (40, 2) | (80, 1):
                return (3900, 1300, 0)
            case (20, 4) | (40, 3) | (80, 2):
                return (7700, 2600, 0)
            case (25, 2) | (50, 1):
                return (2400, 800, 0)
            case (25, 3) | (50, 2) | (100, 1):
                return (4800, 1600, 0)
            case (25, 4) | (50, 3) | (100, 2):
                return (9600, 3200, 0)
            case (30, 1):
                return (1500, 500, 0)
            case (30, 2) | (60, 1):
                return (2900, 1000, 0)
            case (30, 3) | (60, 2):
                return (5800, 2000, 0)
            case (30, 4) | (60, 3):
                return (11600, 3900, 0)
            case (70, 1):
                return (3400, 1200, 0)
            case (70, 2):
                return (6800, 2300, 0)
            case (90, 1):
                return (4400, 1500, 0)
            case (90, 2):
                return (8700, 2900, 0)
            case (110, 1):  # theoretical
                return (5300, 1800, 0)
            case (110, 2):
                return (10600, 3600, 0)
            case (fu, han) if han == 5 or (fu >= 40 and han == 4) or (fu >= 70 and han == 3):
                return (12000, 4000, 0)
            case (_, han) if 6 <= han <= 7:
                return (18000, 6000, 0)
            case (_, han) if 8 <= han <= 10:
                return (24000, 8000, 0)
            case (_, han) if 11 <= han <= 12:
                return (36000, 12000, 0)
            case (_, han) if han >= 13:
                return (48000, 16000, 0)
            case _:
                raise ValueError(f"impossible combination of {fu} fu and {han} han")
    else:
        match (fu, han):
            case (20, 2) | (40, 1):
                return (1300, 400, 700)
            case (20, 3) | (40, 2) | (80, 1):
                return (2600, 700, 1300)
            case (20, 4) | (40, 3) | (80, 2):
                return (5200, 1300, 2600)
            case (25, 2) | (50, 1):
                return (1600, 400, 800)
            case (25, 3) | (50, 2) | (100, 1):
                return (3200, 800, 1600)
            case (25, 4) | (50, 3) | (100, 2):
                return (6400, 1600, 3200)
            case (30, 1):
                return (1000, 300, 500)
            case (30, 2) | (60, 1):
                return (2000, 500, 1000)
            case (30, 3) | (60, 2):
                return (3900, 1000, 2000)
            case (30, 4) | (60, 3):
                return (7700, 2000, 3900)
            case (70, 1):
                return (2300, 600, 1200)
            case (70, 2):
                return (4500, 1200, 2300)
            case (90, 1):
                return (2900, 800, 1500)
            case (90, 2):
                return (5800, 1500, 2900)
            case (110, 1):  # theoretical
                return (3600, 900, 1800)
            case (110, 2):
                return (7100, 1800, 3600)
            case (fu, han) if han == 5 or (fu >= 40 and han == 4) or (fu >= 70 and han == 3):
                return (8000, 2000, 4000)
            case (_, han) if 6 <= han <= 7:
                return (12000, 3000, 6000)
            case (_, han) if 8 <= han <= 10:
                return (16000, 4000, 8000)
            case (_, han) if 11 <= han <= 12:
                return (24000, 6000, 12000)
            case (_, han) if han >= 13:
                return (32000, 8000, 16000)
            case _:
                raise ValueError(f"impossible combination of {fu} fu and {han} han")


def calc_yakuman(count, oya):
    if oya:
        return (48000 * count, 16000 * count, 0)
    else:
        return (32000 * count, 8000 * count, 16000 * count)