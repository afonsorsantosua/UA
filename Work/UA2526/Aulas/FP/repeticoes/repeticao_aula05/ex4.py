

def allMatches(teams):
    assert len(teams) >= 2
    combinacoes = []
    for index, team in enumerate(teams):
        for visitante in teams:
            combinacoes.append((team, visitante))
            if team == visitante:
                combinacoes.remove((team, visitante))

    return combinacoes

teams = ["FCP", "SCP", "SLB"]
print(allMatches(teams))
