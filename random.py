def rounds(coins):
    if (coins < 1):
        return None

    if coins == 1:
        return 1

    round_number = rounds(coins // 2) + 1

    return round_number


t =int(input())


print("It took {0} rounds to change {1} coins into 1".format(rounds(t), t))
