import random

def create_character():
    name = input("Sisesta oma tegelase nimi: ")
    character = {
        "nimi": name,
        "tase": 1,
        "elud": 100,
        "jõud": 10,
        "kaitse": 5,
        "koge": 0,
        "kuld": 50,
        "inventory": {"tervisejook": 0, "mõõk": 0, "soomus": 0}
    }
    return character

def battle(character):
    enemy = {
        "nimi": "Metsik koletis",
        "elud": random.randint(20, 50),
        "jõud": random.randint(5, 15)
    }
    print(f"Sa kohtasid vaenlast: {enemy['nimi']}! Elud: {enemy['elud']}, Jõud: {enemy['jõud']}")
    
    while enemy["elud"] > 0 and character["elud"] > 0:
        action = input("Kas tahad rünnata (r), kasutada eset (k) või põgeneda (p)? ").lower()
        if action == "r":
            damage = max(character["jõud"] - random.randint(0, 5), 1)
            enemy["elud"] -= damage
            print(f"Sa ründasid ja tegid {damage} kahju! Vaenlasel jäi {enemy['elud']} elupunkti.")
            
            if enemy["elud"] > 0:
                enemy_damage = max(enemy["jõud"] - character["kaitse"], 1)
                character["elud"] -= enemy_damage
                print(f"Vaenlane ründas ja tegi {enemy_damage} kahju! Sul on alles {character['elud']} elupunkti.")
        elif action == "k":
            use_item(character)
        elif action == "p":
            print("Sa põgenesid lahingust!")
            return
    
    if character["elud"] > 0:
        print("Sa võitsid lahingu ja said 10 kogemust ning 20 kulda!")
        character["koge"] += 10
        character["kuld"] += 20
        if character["koge"] >= 20:
            character["tase"] += 1
            character["jõud"] += 5
            character["kaitse"] += 2
            character["koge"] = 0
            print(f"Tase tõusis! Oled nüüd {character['tase']}. tasemel.")
    else:
        print("Sa kaotasid lahingu...")

def shop(character):
    print("Tere tulemast poodi! Siin saad osta esemeid.")
    items = {"tervisejook": 30, "mõõk": 50, "soomus": 40}
    print("Saadaval esemed:")
    for item, price in items.items():
        print(f"{item}: {price} kulda")
    
    choice = input("Mida soovid osta? (või kirjuta 'lahku' lahkumiseks): ").lower()
    if choice in items:
        if character["kuld"] >= items[choice]:
            character["kuld"] -= items[choice]
            character["inventory"][choice] += 1
            print(f"Ostsid {choice}! Sinu kuld: {character['kuld']}")
        else:
            print("Sul pole piisavalt kulda!")
    elif choice == "lahku":
        return
    else:
        print("Vale valik.")

def view_inventory(character):
    print("Sinu inventar:")
    print(f"Kuld: {character['kuld']}")
    for item, count in character["inventory"].items():
        print(f"{item}: {count}")

def use_item(character):
    view_inventory(character)
    
    choice = input("Mida soovid kasutada? (või kirjuta 'lahku' lahkumiseks): ").lower()
    if choice == "tervisejook" and character["inventory"]["tervisejook"] > 0:
        character["elud"] += 20
        character["inventory"]["tervisejook"] -= 1
        print(f"Kasutasid tervisejoogi! Sinu elud: {character['elud']}")
    elif choice in character["inventory"] and character["inventory"][choice] > 0:
        print(f"Ei saa praegu kasutada {choice}.")
    elif choice == "lahku":
        return
    else:
        print("Sul pole seda eset!")

def explore(character):
    print("Sa otsustasid maailma avastada...")
    event = random.choice(["leidsid varanduse", "sattusid lõksu", "kohtasid NPC-d"])
    if event == "leidsid varanduse":
        gold = random.randint(10, 50)
        character["kuld"] += gold
        print(f"Sa leidsid varanduse ja said {gold} kulda! Nüüd on sul {character['kuld']} kulda.")
    elif event == "sattusid lõksu":
        damage = random.randint(5, 20)
        character["elud"] -= damage
        print(f"Sattusid lõksu ja kaotasid {damage} elupunkti! Alles on {character['elud']} elupunkti.")
    elif event == "kohtasid NPC-d":
        print("Sa kohtasid rändurit, kes andis sulle tasuta 10 kulda!")
        character["kuld"] += 10

def main():
    character = create_character()
    print(f"Tere tulemast, {character['nimi']}! Sinu seiklused algavad nüüd.")
    
    while character.get("elud", 0) > 0:
        action = input("Kas tahad uurida maailma (u), minna poodi (p), vaadata inventari (vi), kasutada eset (i), võidelda (v) või lõpetada mäng (l)? ").lower()
        if action == "u":
            explore(character)
        elif action == "p":
            shop(character)
        elif action == "vi":
            view_inventory(character)
        elif action == "i":
            use_item(character)
        elif action == "v":
            battle(character)
        elif action == "l":
            print("Mäng on lõppenud. Aitäh mängimast!")
            break
        else:
            print("Tundmatu käsk. Palun proovi uuesti.")

if __name__ == "__main__":
    main()