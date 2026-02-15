import os
import json
from datetime import datetime, timezone

#IdeaVault by Dom: This Tool is for me, and idiot with way to many ideas.

#load data from json
class ValidationError(Exception):
    pass


def validate_idea_structure(idea):
    required_keys = [
        "id", "created_at", "updated_at",
        "last_event_id", "title", "description",
        "category", "status",
        "potential", "effort",
        "next_step", "next_review_at",
        "history"
    ]



    #required keys check
    for key in required_keys:
        if key not in idea:
            raise ValidationError(f"Required key {key} is missing")

    #Category check
    allowed_categories = ["Python", "Server", "Game", "Pokemon", "Life", "Work"]
    if idea["category"] not in allowed_categories:
        raise ValidationError(f"Category must be one of {allowed_categories}")

    #History structure Check

    if not isinstance(idea["history"], list) or len(idea["history"]) == 0:
        raise ValidationError(f"History must be a non-empty List!")

    last_event = idea["history"][-1]
    if not isinstance(last_event, dict):
        raise ValidationError(f"last history entry must be an object/dict")

    #Required last_event keys BEFORE accessing
    if "event_id" not in last_event or "at" not in last_event:
        raise ValidationError("Last history entry must include 'event_id' and 'at'")

    #Validate event_id format
    eid = last_event["event_id"]

    if not isinstance(eid, str) or not eid:
        raise ValidationError("event_id must be a non-empty string")

    if not eid.startswith("EVT-") or not eid[4:].isdigit():
        raise ValidationError("event_id must look like 'EVT-000001'")

    #Validate Timestamp presence/type

    if not isinstance(last_event["at"], str) or not last_event["at"]:
        raise ValidationError(f"timestamp must be a non-empty String!")

    #cross-field integrity

    if idea["last_event_id"] != last_event["event_id"]:
        raise ValidationError(f"last_event_id does not match last History entry")

    if idea["updated_at"] != last_event["at"]:
        raise ValidationError(f" updated_at does not match last event timestamp")


    #Potential type + Range

    if not isinstance(idea["potential"], int):
        raise ValidationError(f"potential must be an Integer!")

    if not (1 <= idea["potential"] <= 10):
        raise ValidationError(f"potential must be between 1 and 10!")


    #Revisit Rule
    if idea["next_review_at"] is not None and idea["effort"] is None:
        raise ValidationError(f"If next_review_at is set, effort must not be None!")

def get_current_time_ISO():
    return datetime.now(timezone.utc).isoformat(timespec="seconds")

print (get_current_time_ISO())

def next_idea_id(ideas_dir: str = "ideas") -> str:
    os.makedirs(ideas_dir, exist_ok=True)

    max_n = 0
    for filename in os.listdir(ideas_dir):
        if filename.startswith("IDEA-") and filename.endswith(".json"):
            num_part = filename[5:-5]  #strip away IDEA and JSON
            if num_part.isdigit():
                max_n = max(max_n, int(num_part))


    return f"IDEA-{max_n + 1:06d}"


def load_idea(idea_id):
    path = f"ideas/{idea_id}.json"

    try:
        with open(path, "r") as f:
            idea = json.load(f)

    except FileNotFoundError:
        raise ValueError(f"Idea file not found: {path}")

    except json.decoder.JSONDecodeError:
        raise ValueError(f"Invalid JSON Format in {path}")

    validate_idea_structure(idea)

    return idea

#creates a new Idea JSON file.
def create_idea(
        title: str,
        description: str,
        category: str,
        potential: int,
        next_step: str,
        effort = None,
        next_review_at = None,
        tags = None,
        ideas_dir: str = "ideas",
) -> str:
    if tags is None:
        tags = []

    idea_id = next_idea_id (ideas_dir)
    ts = get_current_time_ISO()

    idea = {
        "id": idea_id,
        "created_at": ts,
        "updated_at": ts,
        "last_event_id": "EVT-000001",

        "title": title,
        "description": description,
        "category": category,
        "status": "new",

        "potential": potential,
        "effort": effort,  # None allowed
        "next_step": next_step,
        "next_review_at": next_review_at,  # None allowed
        "tags": tags,

        "history": [
            {
                "event_id": "EVT-000001",
                "at": ts,
                "type": "created",
                "note": "Initial capture"
            }
        ]
    }

    validate_idea_structure(idea)

    path = os.path.join(ideas_dir, f"{idea_id}.json")
    with open(path, "w", encoding="utf-8") as f:
        json.dump(idea, f, ensure_ascii=False, indent=2)

    return idea_id



# print(create_idea(
#      title = input("Whats the Title of this Idea: ").strip().capitalize(),
#      description = input("describe the Idea: ").strip().capitalize(),
#      category = input("Category: ").strip().capitalize(),
#      potential = int(input("input the potential as a Number can also be None")),
#      next_step = input("whats the next step?: ").strip().capitalize()
# ))

#def update_idea_potential():

#def change_idea_status():

def show_idea():
    input_number = int(input("Input the Idea Number: "))
    idea_id = f"IDEA-{input_number:06d}"
    idea = load_idea(idea_id)
    print (json.dumps(idea, ensure_ascii=False, indent=2))

print (show_idea())


#def show_idea_history():

