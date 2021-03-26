
import sc2
from sc2 import Race, Difficulty
from sc2.player import Bot, Computer
from sc2.player import Human
from sc2.ids.unit_typeid import UnitTypeId
from sc2.ids.ability_id import AbilityId
from sc2.unit import Unit
from sc2.units import Units
from sc2.position import Point2


class CyclonePush(sc2.BotAI):
    async def on_step(self, iteration: int):
        if iteration == 0:
            for worker in self.workers:
                worker.attack(self.enemy_start_locations[0])
class WorkerRushBot(sc2.BotAI):
    async def on_step(self, iteration: int):
        CCs: Units = self.townhalls(UnitTypeId.COMMANDCENTER)
        cc: Unit = CCs.first
        if self.can_afford(UnitTypeId.ENGINEERINGBAY2):
                # This picks a near-random worker to build a depot at location
                # 'from command center towards game center, distance 8'
                await self.build(UnitTypeId.ENGINEERINGBAY2, near=cc.position.towards(self.game_info.map_center, 8))
 #       if self.can_afford(UnitTypeId.ARMORY2) and self.already_pending(UnitTypeId.SUPPLYDEPOT) < 2:
                # This picks a near-random worker to build a depot at location
                # 'from command center towards game center, distance 8'
 #               await self.build(UnitTypeId.ARMORY2, near=cc.position.towards(self.game_info.map_center, 8))

def main():
    sc2.run_game(
        sc2.maps.get("沙漠风暴经典版work"),
        [
            # Human(Race.Terran),
            Bot(Race.Terran, WorkerRushBot()),
            Bot(Race.Terran, CyclonePush()),
            #Computer(Race.Zerg, Difficulty.Easy),
        ],
        realtime=False,
     )


if __name__ == "__main__":
    main()
