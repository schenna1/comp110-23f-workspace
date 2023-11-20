"""Simulate a river example."""

# from exercises.ex08.bear import Bear
# from exercises.ex08.fish import Fish
from exercises.ex08.river import River

river: River = River(10, 2)
river.view_river()

river.one_river_week()