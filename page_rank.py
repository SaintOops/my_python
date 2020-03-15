links = [("a", "b"), ("a", "c"), ("b", "c")]
k = 1
pages = ["a","b","c"]
ranks = {"a":1,"b":1,"c":1}
while k != 10:
    for i in links:
        for j in i:
            ranks[j] = ranks[pages[links.index(i)]] / len(i)
        ranks[pages[links.index(i)]] *= 0.85
    k += 1
