def overlap(s,t):
    """sとtの重なりの長さ"""
    m = len(s)
    n = max(0, m-len(t))
    for i in range(n,m):
        if s[i:] == t[:m-i]:
            return m-i
    return 0

def shortest_superstring(words):
    """最短超文字列問題"""
    from ortoolpy import tsp
    words = ['']+words
    n = len(words)
    dist = {(i,j):len(t)-overlap(s,t) for i,s in enumerate(words)
            for j,t in enumerate(words) if i != j}
    _,lst = tsp(words,dist)
    return ''.join(words[j][len(words[j])-dist[i,j]:] for i,j in zip(lst,lst[1:]))

ans = shortest_superstring('subway dentist wayward highway terrible english blessed warden stash shunt hunter'.split())
print(ans)