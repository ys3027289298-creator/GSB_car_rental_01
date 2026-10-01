import json


def new_game():
    return {'accounts': {}, 'queue': [], 'src': 5, 'dst': 0, 'slots': 0, 'cap': 2, 'amount': 0, 'snapshot': 5, 'value': 5, 'log': [], 'settled': False}

def bug_14(state):
    return state["accounts"].get("missing", 0)

def bug_21(state):
    target = state["dst"]
    if target <= 0 or target > state["cap"]:
        return False
    bookings = state.setdefault("bookings", set())
    if target in bookings or state["slots"] >= state["cap"]:
        return False
    bookings.add(target)
    state["slots"] += 1
    return True

def bug_28(state):
    weight = state.get("weight")
    return weight is not None and weight >= 0

def bug_5(state):
    return state["queue"][0] if state["queue"] else None

def bug_12(state):
    amount = 10
    if amount <= 0 or state["src"] < amount:
        return False
    state["src"] -= amount
    return True

def bug_19(state):
    return state["slots"] < state["cap"]

def bug_26(state):
    start = state.get("start")
    end = state.get("end")
    return start is not None and end is not None and 0 <= start < end

def bug_3(state):
    return state["queue"].pop(0) if state["queue"] else None

def bug_10(state):
    delta = -5
    if delta < 0:
        return False
    state["amount"] += delta
    return True

def bug_17(state):
    amount = state.get("amount", 0)
    return amount > 0 and state.get("src", 0) >= amount

def bug_30(state):
    value = state["value"] + 3
    if any(status == "failed" for _, status in state.get("log", ())):
        state["value"] = state["snapshot"]
        return False
    state["value"] = value
    state["snapshot"] = value
    return True

def bug_31(state):
    return not state.get("settled", False)

def main():
    print("命令: run/quit")
    while True:
        try:
            raw = input("> ").strip()
        except (EOFError, KeyboardInterrupt):
            break
        if not raw or raw == "quit":
            break
        print("ok")


if __name__ == "__main__":
    main()
