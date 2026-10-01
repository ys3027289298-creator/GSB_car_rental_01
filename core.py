import json


def new_game():
    return {'accounts': {}, 'queue': [], 'src': 5, 'dst': 0, 'slots': 0, 'cap': 2, 'amount': 0, 'snapshot': 5, 'value': 5, 'log': [], 'settled': False}

def bug_14(state):
    return state["accounts"].get("missing", -1)

def bug_21(state):
    return True

def bug_28(state):
    return True

def bug_5(state):
    return state["queue"].pop(0)

def bug_12(state):
    state["src"] -= 10
    return True

def bug_19(state):
    return True

def bug_26(state):
    return True

def bug_3(state):
    return state["queue"].pop()

def bug_10(state):
    state["amount"] += -5
    return True

def bug_17(state):
    return True

def bug_30(state):
    return True

def bug_31(state):
    return True

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
