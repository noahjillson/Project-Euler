if __name__ == "__main__":
    prime_count = 0
    i = 2
    while prime_count < 6:
        for x in range(3, i, 2):
            if i % x == 0:
                i += 1
                x = 3
        i += 1
        prime_count += 1
    print(i)
    
