from __future__ import annotations

from typing import Optional, TYPE_CHECKING

import actions
import color
import components.ai
import components.inventory
from components.base_component import BaseComponent
from exceptions import Impossible
from input_handlers import (
    ActionOrHandler,
    AreaRangedAttackHandler,
    SingleRangedAttackHandler,
)

if TYPE_CHECKING:
    from entity import Actor, Ability


class Spell(BaseComponent):
    parent: Ability

    def get_action(self, spell_user: Actor) -> Optional[actions.Action]:
        """Try to return the action for this ability."""
        return actions.AbilityAction(spell_user, self.parent)

    def activate(self, action: actions.AbilityAction) -> None:
        """Invoke the ability.

        `action` is the context for this activation.
        """
        raise NotImplementedError()


class HealingSpell(Spell):
    def __init__(self, amount: int):
        self.amount = amount

    def activate(self, action: actions.AbilityAction) -> None:
        spell_user = action.entity
        amount_recovered = spell_user.fighter.heal_hp(self.amount)

        if amount_recovered > 0:
            self.engine.message_log.add_message(
                f"You consume the {self.parent.name}, and recover {amount_recovered} HP!",
                color.health_recovered,
            )
        else:
            raise Impossible(f"Your health is already full.")
