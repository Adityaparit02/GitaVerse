from state_manager import StateManager

state = StateManager("state/current_verse.json")

print("Current :", state.get_current_id())

state.increment(700)

print("Updated :", state.get_current_id())