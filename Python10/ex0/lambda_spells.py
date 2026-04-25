def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    sorted_list = sorted(artifacts, key=lambda artifact: artifact["power"],
                         reverse=True)
    return sorted_list


def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    filtered_list = filter(lambda mage: mage["power"] >= min_power, mages)
    return list(filtered_list)


def spell_transformer(spells: list[str]) -> list[str]:
    transformed = map(lambda spell: "*" + spell + "*", spells)
    return list(transformed)


def mage_stats(mages: list[dict]) -> dict:
    mage_stat = {}
    mage_stat["max_power"] = max(map(lambda mage: mage["power"], mages))
    mage_stat["min_power"] = min(map(lambda mage: mage["power"], mages))
    mage_stat["avg_power"] = (round(sum(map(lambda mage: mage["power"],
                                            mages)) / len(mages), 2)
                              if mages else 0)
    return mage_stat


if __name__ == "__main__":
    artifacts = [{'name': 'Crystal Orb', 'power': 93, 'type': 'weapon'},
                 {'name': 'Light Prism', 'power': 86, 'type': 'relic'},
                 {'name': 'Wind Cloak', 'power': 98, 'type': 'armor'},
                 {'name': 'Crystal Orb', 'power': 67, 'type': 'accessory'}]
    mages = [{'name': 'Sage', 'power': 99, 'element': 'shadow'},
             {'name': 'Nova', 'power': 79, 'element': 'lightning'},
             {'name': 'Zara', 'power': 88, 'element': 'water'},
             {'name': 'River', 'power': 87, 'element': 'ice'},
             {'name': 'Phoenix', 'power': 52, 'element': 'ice'}]
    spells = ['lightning', 'shield', 'darkness', 'earthquake']
    print("Testing artifact sorter...")
    print("Before sort:")
    print(artifacts)
    print("After sort")
    print(artifact_sorter(artifacts))
    for artifact, s_artifact in zip(artifacts, artifact_sorter(artifacts)):
        if artifact != s_artifact:
            print(f"{s_artifact["name"]} ({s_artifact["power"]} power) comes"
                  f" before {artifact["name"]} ({artifact["power"]} power)")
            break
    print("Before filter:")
    print(mages)
    print("Minimum power is 80")
    print("After filter:")
    print(power_filter(mages, 80))
    print("\nTesting spell transformer....")
    for spell in spell_transformer(spells):
        print(spell + " ", end="")
    print("\nMage statistics:")
    print(mage_stats(mages))
