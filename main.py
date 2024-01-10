def check_relation(net, first, second):
    graph = {}
    for connection in net:
        user1, user2 = connection
        if user1 not in graph:
            graph[user1] = []
        if user2 not in graph:
            graph[user2] = []
        graph[user1].append(user2)
        graph[user2].append(user1)

    visited = set()

    def dfs(user, target):
        print(f"Visiting {user}")
        visited.add(user)
        if user == target:
            return True
        for friend in graph[user]:
            if friend not in visited:
                if dfs(friend, target):
                    return True
        return False

    result = dfs(first, second)
    print(f"Result: {result}")
    return result

if __name__ == '__main__':
    net = (
        ("Нурбакыт", "Арслан"), ("Жанар", "Эмир"),
        ("Бегимай", "Улук"), ("Эрнис", "Мырза"),
        ("Талгат", "Айдар"), ("Таалай", "Айнуска"),
        ("Назима", "Айжан"), ("Ислам", "Махабат"),
        ("Нурсултан", "Айжаркын"), ("Элиза", "Алибек")
    )

    assert check_relation(net, "Нурбакыт", "Айжаркын") is False
    assert check_relation(net, "Элиза", "Эмир") is False
    assert check_relation(net, "Махабат", "Таалай") is False
    assert check_relation(net, "Айнуска", "Ислам") is False
    assert check_relation(net, "Нурсултан", "Бегимай") is False
    assert check_relation(net, "Талгат", "Эрнис") is False
    assert check_relation(net, "Айдар", "Мырза") is False

