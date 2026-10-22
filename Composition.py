class LowHealthBoost:
    """Pluggable behavior component."""
    def apply(self, base_damage: int, health_pct: float) -> int:
        multiplier = 1.0 + (1.0 - health_pct)
        return int(base_damage * multiplier)


class Character:
    """Character delegates damage calculation to a component."""
    def __init__(self, name: str, base_damage: int, modifier=None):
        self.name = name
        self.base_damage = base_damage
        self.health_pct = 1.0
        self.modifier = modifier  # Composition: HAS-A modifier

    def get_damage(self) -> int:
        if self.modifier:
            return self.modifier.apply(self.base_damage, self.health_pct)
        return self.base_damage


# Usage
hero = Character("Warrior", 50)

# Swap behavior dynamically by composing with a modifier
berserker = Character("Barbarian", 50, modifier=LowHealthBoost())
berserker.health_pct = 0.2  # 20% HP remaining

print(f"{hero.name} Damage:", hero.get_damage())        # Output: 50
print(f"{berserker.name} Damage:", berserker.get_damage()) # Output: 90
