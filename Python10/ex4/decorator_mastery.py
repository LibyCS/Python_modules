from typing import Callable
from functools import wraps
import time
from random import randint


def spell_timer(func: Callable) -> Callable:
    """
    Decorator that prints some statements and times
    how along it takes to execute the function"""
    @wraps(func)
    def wrapper(*args) -> str:
        """
        Wrapper which executes before the function and the function
        """
        print(f"Casting {func.__name__}...")
        start = time.time()
        result = func(*args)
        print(f"Spell completed in {(time.time() - start):.3f} seconds")
        return result
    return wrapper


def power_validator(min_power: int) -> Callable:
    """
    Takes in the minimum power
    """
    def decorator(func: Callable) -> Callable:
        """
        takes in the function it will decorate
        """
        @wraps(func)
        def wrapper(*args, **kwargs) -> str:
            """
            Determines if power is valid or not
            """
            if "power" in kwargs:
                power = kwargs["power"]
            else:
                power = args[2]
            if power < min_power:
                return "Insufficient power for this spell"
            return func(*args, **kwargs)
        return wrapper
    return decorator


def retry_spell(max_attempts: int) -> Callable:
    """
    Takes in the max attempts
    """
    def decorator(func: Callable) -> Callable:
        """
        takes in the function it will decorate
        """
        @wraps(func)
        def wrapper(*args) -> str:
            """
            executes spell till it works or runs out of attempts
            """
            for i in range(max_attempts):
                try:
                    return func(*args)
                except Exception:
                    print("Spell failed, retrying...(attempt "
                          f"{i}/{max_attempts})")
            return f"Spell casting failed after {max_attempts} attempts"
        return wrapper
    return decorator


class MageGuild:
    @staticmethod
    def validate_mage_name(name: str) -> bool:
        if len(name) >= 3 and name.isalpha():
            return True
        return False

    @power_validator(10)
    def cast_spell(self, spell_name: str, power: int) -> str:
        return f"Successfully cast {spell_name} with {power} power"


@spell_timer
def fireball() -> str:
    """
    Spell that returns a string
    """
    return "Fireball cast!"


@power_validator(20)
def crack(power: int) -> str:
    """
    Spell that returns a string
    """
    return f"Crack hits for {power} damage"


@retry_spell(3)
def spell(rate: int) -> str:
    """
    Spell that returns a string
    """
    if randint(1, 100) < 100 - rate:
        raise ValueError
    return "Waaaaaaagh spelled !"


if __name__ == "__main__":
    print("Testing spell timer...")
    print("Result:", fireball())
    print("\nTesting power validator...")
    print("Valid power for minimum power = 20:")
    print("Result:", crack(power=20))
    print("Invalid power for minimum power = 20:")
    print("Result:", crack(power=10))
    print("\nTesting retrying spell...")
    print(spell(10))
    print(spell(100))
    print("\nTesting MageGuild...")
    print(MageGuild.validate_mage_name("Charlie"))
    print(MageGuild.validate_mage_name("An"))
    guild = MageGuild()
    print(guild.cast_spell("Lightning", 15))
    print(guild.cast_spell("Crack", 5))
