"""Write one analysis.json per city, all with the Dallas decisions, so the cities are measured the same way.

Source: the FBI's NIBRS state files (data/raw/<ST>-<year>.zip). Each city is its own police department only. Aggravated
(13A) and simple (13B) assault, individual victims of any age; officers, intimidation and homicide are out. Hispanic of
any race first, otherwise the recorded race. Partner flag from the victim-offender relationship. Black women against
Hispanic, White and Asian women. ORI, Census place and window (by tier) come from out/eligibility.csv via cities.py:
tier 1 runs January 2022 to December 2025, tier 2 January 2024 to December 2025. min_pop stays at the kit default.

  python scripts/make_configs.py      ->  cities/<slug>/analysis.json for each city
"""
import json
import pathlib
import re

from cities import CITIES

ROOT = pathlib.Path(__file__).resolve().parent.parent
STATE = {"AZ": "Arizona", "CA": "California", "CO": "Colorado", "DC": "the District of Columbia", "FL": "Florida", "IL": "Illinois",
         "IN": "Indiana", "KY": "Kentucky", "MA": "Massachusetts", "MD": "Maryland", "MI": "Michigan", "MN": "Minnesota", "MO": "Missouri",
         "NC": "North Carolina", "NE": "Nebraska", "NJ": "New Jersey", "NV": "Nevada", "NY": "New York", "OH": "Ohio", "OK": "Oklahoma",
         "OR": "Oregon", "PA": "Pennsylvania", "TN": "Tennessee", "TX": "Texas", "VA": "Virginia", "WA": "Washington", "WI": "Wisconsin"}
DEPT = {"DCMPD0000": "Metropolitan Police Department", "NY0303000": "New York City Police Department", "OR0260200": "Portland Police Bureau",
        "MOSPD0000": "St. Louis Metropolitan Police Department"}
WEAPONS = [{"label": "Firearm", "keywords": ["FIREARM", "HANDGUN", "RIFLE", "SHOTGUN"]},
           {"label": "Knife or cutting", "keywords": ["KNIFE", "CUTTING"]},
           {"label": "Blunt object or vehicle", "keywords": ["BLUNT", "CLUB", "MOTOR VEHICLE"]},
           {"label": "Hands, fists, feet", "keywords": ["PERSONAL WEAPON", "ASPHYXIATION", "STRANGULATION"]}]


def main():
    for c in CITIES:
        slug, name = c["slug"], c["name"]
        years = f"{c['start'][:4]} to {c['end'][:4]}"
        dept = DEPT.get(c["ori"]) or (c["agency"] if re.search("Police|Sheriff", c["agency"]) else f"{c['agency']} Police Department")
        cfg = {
            "title": f"Assault victims in {name}",
            "author": "Martin Ngoh",
            "place": {"name": name, "short": name, "census_geoid": c["geoid"]},
            "acs_release": "acs2024_5yr",
            "window": {"start": c["start"], "end": c["end"]},
            "event": {"noun": "assault", "plural": "assaults", "verb": "assaulted"},
            "incidents": [{"path": f"data/{slug}_simple.csv", "kind": "simple"}, {"path": f"data/{slug}_aggravated.csv", "kind": "aggravated"}],
            "kind_labels": {"simple": "Simple assault", "aggravated": "Aggravated assault"},
            "columns": {"id": "victim_id", "date": "incident_date", "race": "race_group", "sex": "sex", "age": "age",
                        "premise": "premise", "weapon": "weapon", "code": "offense_code"},
            "race_map": {"B": "Black", "H": "Hispanic", "W": "White", "A": "Asian"},
            "sex_values": {"F": "F", "M": "M"},
            "groups": ["Black", "Hispanic", "White", "Asian"],
            "focus": {"group": "Black", "sex": "F", "label": "Black women"},
            "flags": {"partner": {"column": "partner", "values": ["Y"], "label": "Intimate partner"}},
            "weapon_classes": WEAPONS,
            "sources": [f"FBI National Incident-Based Reporting System (NIBRS) state files for {STATE[c['state']]}, {dept} ({c['ori']}), {years}",
                        "US Census Bureau ACS 2020 to 2024 five-year estimates via Census Reporter"],
            "_ori": c["ori"],
            "_state": c["state"],
            "_tier": c["tier"],
        }
        d = ROOT / "cities" / slug
        d.mkdir(parents=True, exist_ok=True)
        (d / "analysis.json").write_text(json.dumps(cfg, indent=1) + "\n")
    print(f"wrote {len(CITIES)} configs in cities/")


if __name__ == "__main__":
    main()
