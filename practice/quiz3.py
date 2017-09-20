class Monster(object):
    def __init__(self, name, hp, damage):
        self.name = name
        self.damage = damage
        self.hp = hp

    def attack(self, target):
        target.hp -= self.damage
        if target.hp <= 0:
            info = f"{target.name}(이)가 죽었다."
        else:
            info = f"{target.name}의 남은 체력 {target.hp}"

        print(f"{self.name}가 {target.name}을 공격해 {self.damage}의 피해를 입혔다.")
        print(info)
        return None

    def __str__(self):
        return f"{self.name}: 공격력 {self.damage} 체력 {self.hp}"


pikachu = Monster('피카츄', 130, 130)
ggobugi = Monster('꼬부기', 150, 100)

print(pikachu)
print(ggobugi)

pikachu.attack(ggobugi)
# ggobugi.attack(pikachu)
