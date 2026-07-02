import random
from pathlib import Path

import pandas as pd

# ---------------- CONFIG ---------------- #

NUMBER_OF_PROPERTIES = 2000

OUTPUT_PATH = Path(__file__).resolve().parent.parent / "data" / "properties.csv"

COMMUNITIES = {
    "Dubai Marina": {
        "price": (1500000, 5000000),
        "roi": (7.0, 9.0),
        "yield": (6.5, 8.5),
        "risk": "Low",
        "appreciation": "High"
    },
    "JVC": {
        "price": (650000, 2000000),
        "roi": (8.0, 10.0),
        "yield": (7.5, 9.0),
        "risk": "Medium",
        "appreciation": "Medium"
    },
    "Business Bay": {
        "price": (1200000, 4500000),
        "roi": (7.0, 8.8),
        "yield": (6.5, 8.2),
        "risk": "Low",
        "appreciation": "High"
    }
}

DEVELOPERS = [
    "Emaar",
    "DAMAC",
    "Sobha Realty",
    "Binghatti",
    "Danube"
]

PROPERTY_TYPES = [
    "Apartment",
    "Villa",
    "Townhouse"
]

BEDROOMS = [
    "Studio",
    "1 BR",
    "2 BR",
    "3 BR",
    "4 BR"
]

PREFIXES = [
    "Marina",
    "Azure",
    "Skyline",
    "Elite",
    "Palm",
    "Creek",
    "Canal",
    "Vista",
    "Royal",
    "Grand",
    "Park",
    "Harbour",
    "Ocean",
    "Infinity",
    "Central",
    "The"
]

SUFFIXES = [
    "Heights",
    "Residences",
    "Gardens",
    "Tower",
    "Point",
    "Square",
    "Place",
    "Vista",
    "Horizon",
    "Residence",
    "One",
    "Central",
    "Park",
    "View",
    "Collection",
    "Living"
]

properties = []

for i in range(1, NUMBER_OF_PROPERTIES + 1):

    community = random.choice(list(COMMUNITIES.keys()))
    info = COMMUNITIES[community]

    price = random.randint(info["price"][0], info["price"][1])

    roi = round(random.uniform(info["roi"][0], info["roi"][1]), 1)

    rental = round(random.uniform(info["yield"][0], info["yield"][1]), 1)

    property_name = (
        random.choice(PREFIXES)
        + " "
        + random.choice(SUFFIXES)
    )

    properties.append({

        "Property_ID": f"PID-{i:05}",

        "Property": property_name,

        "Community": community,

        "Developer": random.choice(DEVELOPERS),

        "Property_Type": random.choice(PROPERTY_TYPES),

        "Bedrooms": random.choice(BEDROOMS),

        "Price_AED": price,

        "ROI": f"{roi}%",

        "Rental_Yield": f"{rental}%",

        "Expected_Appreciation": info["appreciation"],

        "Risk": info["risk"]

    })

df = pd.DataFrame(properties)

OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)

df.to_csv(OUTPUT_PATH, index=False)

print("=" * 50)
print("✅ Dataset generated successfully!")
print(f"Properties: {len(df)}")
print(f"Saved to: {OUTPUT_PATH}")
print("=" * 50)