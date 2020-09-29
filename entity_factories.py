from components.ai import HostileEnemy
from components import consumable, equippable, spell
from components.equipment import Equipment
from components.fighter import Fighter
from components.inventory import Inventory
from components.ability_menu import Ability_Menu
from components.level import Level
from entity import Actor, Item, Ability

player = Actor(
    char="@",
    color=(255, 255, 255),
    name="Player",
    ai_cls=HostileEnemy,
    equipment=Equipment(),
    fighter=Fighter(hp=30, bp=10, base_defense=1, base_power=2),
    inventory=Inventory(capacity=26),
    level=Level(level_up_base=200),
    ability_menu=Ability_Menu(capacity=26)
)

orc = Actor(
    char="o",
    color=(63, 127, 63),
    name="Orc",
    ai_cls=HostileEnemy,
    equipment=Equipment(),
    fighter=Fighter(hp=30, bp=5, base_defense=1, base_power=2),
    inventory=Inventory(capacity=0),
    level=Level(xp_given=35),
    ability_menu=Ability_Menu(capacity=0)
)

troll = Actor(
    char="T",
    color=(0, 127, 0),
    name="Troll",
    ai_cls=HostileEnemy,
    equipment=Equipment(),
    fighter=Fighter(hp=16, bp=10, base_defense=1, base_power=4),
    inventory=Inventory(capacity=0),
    level=Level(xp_given=100),
    ability_menu=Ability_Menu(capacity=0)
)

confusion_scroll = Item(
    char="~",
    color=(207, 63, 255),
    name="Confusion Scroll",
    consumable=consumable.ConfusionConsumable(number_of_turns=10),
)

fireball_scroll = Item(
    char="~",
    color=(255, 0, 0),
    name="Fireball Scroll",
    consumable=consumable.FireballDamageConsumable(damage=12, radius=3),
)

health_potion = Item(
    char="!",
    color=(127, 0, 255),
    name="Health Potion",
    consumable=consumable.HealingConsumable(amount=4),
)

blood_potion = Item(
    char="!",
    color=(255, 0, 0),
    name="Bottled Blood",
    consumable=consumable.BloodConsumable(amount=4),
)

lightning_scroll = Item(
    char="~",
    color=(255, 255, 0),
    name="Lightning Scroll",
    consumable=consumable.LightningDamageConsumable(damage=20, maximum_range=5),
)

dagger = Item(
    char="/", color=(0, 191, 255), name="Dagger", equippable=equippable.Dagger()
)

sword = Item(
    char="/", color=(0, 191, 255), name="Sword", equippable=equippable.Sword()
)

leather_armor = Item(
    char="[",
    color=(139, 69, 19),
    name="Leather Armor",
    equippable=equippable.LeatherArmor(),
)

chain_mail = Item(
    char="[", color=(139, 69, 19), name="Chain Mail", equippable=equippable.ChainMail()
)

health_spell = Ability(
    char="!",
    color=(255, 0, 0),
    name="Blood Heal",
    spell=spell.HealingSpell(amount=4),
)
