from __future__ import print_function
import draft

combine = draft.DraftCombineDrill('2013-14')
print("Combine Drill")
print(combine.results())

anthro = draft.DraftAnthro('2013-14')
print("Anthro")
print(anthro.results())

stationary_shooting = draft.DraftStationaryShooting('2013-14')
print("Stationary Shooting")
print(stationary_shooting.results())

spot_shooting = draft.DraftSpotShooting('2013-14')
print("Spot Shooting")
print(spot_shooting.results())

combine_stats = draft.DraftCombineStats('2013-14')
print("Combine")
print(combine_stats.results())
