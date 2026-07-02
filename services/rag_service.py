from pathlib import Path
import pandas as pd

BASE_DIR = Path(__file__).resolve().parent.parent

csv_path = BASE_DIR / "data" / "properties.csv"

properties = pd.read_csv(csv_path)


def calculate_score(row):

    score = 0

    # ROI
    roi = float(str(row["ROI"]).replace("%", ""))
    score += roi * 5

    # Rental Yield
    rental = float(str(row["Rental_Yield"]).replace("%", ""))
    score += rental * 4

    # Expected Appreciation
    appreciation = str(row["Expected_Appreciation"])

    if appreciation == "High":
        score += 20
    elif appreciation == "Medium":
        score += 10

    # Risk
    if row["Risk"] == "Low":
        score += 20
    elif row["Risk"] == "Medium":
        score += 10

    return round(score, 1)


def search_properties(
    budget,
    property_type=None,
    risk=None,
    community=None
):

    filtered = properties.copy()

    filtered = filtered[
        filtered["Price_AED"] <= budget
    ]

    if property_type and property_type != "Any":
        filtered = filtered[
            filtered["Property_Type"] == property_type
        ]

    if risk and risk != "Any Risk":
        filtered = filtered[
            filtered["Risk"] == risk
        ]

    if community and community != "Any Community":
        filtered = filtered[
            filtered["Community"].str.contains(
                community,
                case=False,
                na=False
            )
        ]

    if filtered.empty:
        return filtered

    filtered["Investment_Score"] = filtered.apply(
        calculate_score,
        axis=1
    )

    filtered = filtered.sort_values(
        "Investment_Score",
        ascending=False
    )

    return filtered