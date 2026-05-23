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
class WarthunderAirArchipelagoOptions:
    pass

# Main Class
class WarthunderAirGame(Game):
    name = "WarThunderAir"
    platform = KeymastersKeepGamePlatforms.PC

    platforms_other = [
        KeymastersKeepGamePlatforms.PS4,
        KeymastersKeepGamePlatforms.PS5,
        KeymastersKeepGamePlatforms.XONE,
        KeymastersKeepGamePlatforms.XSX,
    ]

    is_adult_only_or_unrated = False

    options_cls = WarthunderAirArchipelagoOptions

    # Optional Game Constraints
    def optional_game_constraint_templates(self) -> List[GameObjectiveTemplate]:
        return [
            GameObjectiveTemplate(
                label="Cannot use VEHICLETYPE",
                data={
                    "VEHICLETYPE": (self.vehicletypes, 1),
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
                weight=12,
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
                label="Win a battle using VEHICLETYPE",
                data={
                    "VEHICLETYPE": (self.vehicletypes, 1),
                },
                weight=5,
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
                label="Destroy BASES bases in a battle",
                data={
                    "BASES": (self.bases, 1),
                },
                weight=5,
            ),
            GameObjectiveTemplate(
                label="Destroy TARGET ground targets in a battle",
                data={
                    "TARGET": (self.target, 1),
                },
                weight=5,
            ),
        ]

    # Datasets
    @staticmethod
    def vehicletypes() -> List[str]:
        return [
            "Fighter",
            "Strike Aircraft",
            "Bomber",
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
            "13.0",
            "13.3",
            "13.7",
            "14.0",
            "14.3",
            "14.7",
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
    def target() -> range:
        return range(5, 15)
    
    @staticmethod
    def bases() -> range:
        return range(1, 4)

    # picks a random number from 20-30
    @staticmethod
    def enemy_count() -> range:
        return range(2, 5)
