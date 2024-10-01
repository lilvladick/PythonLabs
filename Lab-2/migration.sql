CREATE TABLE IF NOT EXISTS travel_costs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    vehicle_type TEXT NOT NULL,
    fuel_consumption REAL NOT NULL,
    weight REAL NOT NULL,
    distance REAL NOT NULL,
    fuel_type TEXT NOT NULL,
    travel_cost REAL NOT NULL
);