from __future__ import annotations

import functools
from typing import List, Dict, Set

from dataclasses import dataclass

from Options import Toggle, OptionSet

from ..game import Game
from ..game_objective_template import GameObjectiveTemplate

from ..enums import KeymastersKeepGamePlatforms


# Option Dataclass
@dataclass
class WarthunderGroundArchipelagoOptions:
    pass

# Main Class
class WarthunderGroundGame(Game):
    name = "WarThunderGround"
    platform = KeymastersKeepGamePlatforms.PC

    platforms_other = [
        KeymastersKeepGamePlatforms.PS4,
        KeymastersKeepGamePlatforms.PS5,
        KeymastersKeepGamePlatforms.XONE,
        KeymastersKeepGamePlatforms.XSX,
    ]

    is_adult_only_or_unrated = False

    options_cls = WarthunderGroundArchipelagoOptions

    # Optional Game Constraints
    def optional_game_constraint_templates(self) -> List[GameObjectiveTemplate]:
        return [
            GameObjectiveTemplate(
                label="Cannot use VEHICLETYPE",
                data={
                    "VEHICLETYPE": (self.vehicletypes2, 1),
                },
            ),
        ]

    # Main Objectives
    def game_objective_templates(self) -> List[GameObjectiveTemplate]:
        return [
            GameObjectiveTemplate(
                label="Win a battle at br BATTLERATING",
                data={
                    "BATTLERATING": (self.battlerating, 1),
                },
                weight=10,
            ),
            GameObjectiveTemplate(
                label="Win a battle as NATION",
                data={
                    "NATION": (self.nations, 1),
                },
                weight=10,
            ),
            GameObjectiveTemplate(
                label="Get KILLS kills in a battle",
                data={
                    "KILLS": (self.enemy_count, 1),
                },
                weight=10,
            ),
            GameObjectiveTemplate(
                label="Win a battle using only VEHICLETYPE",
                data={
                    "VEHICLETYPE": (self.vehicletypes, 1),
                },
                weight=5,
            ),
            GameObjectiveTemplate(
                label="Win a battle using only VEHICLETYPE",
                data={
                    "VEHICLETYPE": (self.vehicletypes2, 2),
                },
                weight=7,
            ),
            GameObjectiveTemplate(
                label="Get KILLS kills as NATION in a battle",
                data={
                    "KILLS": (self.enemy_count, 1),
                    "NATION": (self.nations, 1),
                },
                weight=5,
            ),
            GameObjectiveTemplate(
                label="Get the MEDAL medal AMMOUNT times in a battle",
                data={
                    "MEDAL": (self.medals, 1),
                    "AMMOUNT": (self.ammounts, 1),
                },
                weight=7
            ),
            GameObjectiveTemplate(
                label="Win a Battle by Dropping a Nuke",
                data=dict(),
                weight=1,
            ),
            GameObjectiveTemplate(
                label="Take control of a Capture Point",
                data=dict(),
                weight=7,
            ),
        ]

    # Datasets
    @staticmethod
    def vehicletypes() -> List[str]:
        return [
            "Light Tanks",
            "Medium Tanks",
            "Heavy Tanks",
            "SPGs",
            "SPAAs",
            "Helicopters",
        ]
    
    @staticmethod
    def vehicletypes2() -> List[str]:
        return [
            "Light Tanks",
            "Medium Tanks",
            "Heavy Tanks",
            "SPGs",
            "SPAAs",
            "Helicopters",
            "Aircraft",
        ]
    
    @staticmethod
    def battlerating() -> List[str]:
        return [
            "1.0",
            "1.3",
            "1.7",
            "2.0",
            "2,3",
            "2.7",
            "3.0",
            "3.3",
            "3.7",
            "4.0",
            "4.3",
            "4.7",
            "5.0",
            "5.3",
            "5.7",
            "6.0",
            "6.3",
            "6.7",
            "7.0",
            "7.3",
            "7.7",
            "8.0",
            "8.3",
            "8.7",
            "9.0",
            "9.3",
            "9.7",
            "10.0",
            "10.3",
            "10.7",
            "11.0",
            "11.3",
            "11.7",
            "12.0",
            "12.3",
            "12.7",
        ]
    
    @staticmethod
    def nations() -> List[str]:
        return [
            "USA",
            "USSR(Russia)",
            "Germany",
            "UK",
            "France",
            "Italy",
            "Japan",
            "China",
            "Sweden",
        ]
    
    @staticmethod
    def medals() -> List[str]:
        return [
            "Intelligence",
            "According to Intelligence",
        ]
    
    @staticmethod
    def ammounts() -> List[str]:
        return range(2, 5)

    @staticmethod
    def enemy_count() -> range:
        return range(4, 10)
