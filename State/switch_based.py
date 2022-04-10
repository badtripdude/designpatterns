from enum import Enum, auto


class State(Enum):
    LOCKED = auto()
    FAILED = auto()
    UNLOCKED = auto()


if __name__ == '__main__':
    pin = 1234
    state = State.LOCKED
    while 1:
        if state == State.LOCKED:
            entry = int(input("PIN>>>"))

            if entry == pin:
                state = state.UNLOCKED
            else:
                state = state.FAILED
            continue
        elif state == state.UNLOCKED:
            print('unlocked...')
            break
        elif state == state.FAILED:
            print('fail...')
            state = state.LOCKED
            continue
