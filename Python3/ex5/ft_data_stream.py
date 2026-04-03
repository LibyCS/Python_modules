import typing
import random


def gen_event() -> typing.Generator[tuple[str, str], None, None]:
    """
    Picks a random player and a random action, yields
    a new tuple of name and action everytime next()
    is used on this function.
    """
    players = ["bob", "alice", "dylan", "charlie"]
    actions = ["run", "eat", "sleep", "grab", "move",
               "climb", "swim", "release", "use"]
    while True:
        name = random.choice(players)
        action = random.choice(actions)
        yield (name, action)


def consume_event(events: list) -> typing.Generator[tuple[str, str],
                                                    None, None]:
    """
    Randomly chooses an event from events list and yields
    that randomly chosen event while also deleting it
    from events
    """
    while events:
        event = random.choice(events)
        events.remove(event)
        yield event


def data_stream() -> None:
    """
    Creates 1000 generated events
    then creates 10 generated events in a list
    and removes each event in that list with
    another generator
    """
    print("=== Game Data Stream Processor ===")
    for i in range(1, 1000):
        name, action = next(gen_event())
        print(f"Event {i}: Player {name} did action {action}")
    events: list = []
    for i in range(0, 10):
        events.append(next(gen_event()))
    print(f"Built list of 10 events: {events}")
    consume = consume_event(events)
    for event in consume:
        print(f"Got event from list: {event}")
        print(f"Remains in list: {events}")


if __name__ == "__main__":
    data_stream()
