from gymnasium.envs.registration import register

register(
    id = "shopping_trip/ShoppingTrip-v0",
    entry_point = "shopping_trip.env:shopping_trip_env",
)