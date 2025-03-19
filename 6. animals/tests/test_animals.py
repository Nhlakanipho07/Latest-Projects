import pytest
from animals.animals import (
    Animal,
    Dog,
    Cat,
    Home,
)


def test_no_animal_name():
    with pytest.raises(TypeError) as error_message:
        Animal()
    assert "Animal.__init__() missing 1 required positional argument: 'name'" in str(
        error_message
    )


@pytest.mark.parametrize(
    "invalid_name",
    [{}, (), 123, False, True, 4.3, None, []],
)
def test_invalid_animal_name(invalid_name):
    with pytest.raises(TypeError, match="The name must be a string"):
        Animal(invalid_name)


def test_animal_sound():
    animal = Animal("animal")
    assert animal.sound() == "sound..."


@pytest.mark.parametrize(
    "animal_name, animal_eating",
    [
        ("Fluffy", "Fluffy eats"),
        ("Bella", "Bella eats"),
        ("Daisy", "Daisy eats"),
    ],
)
def test_animal_eating(animal_name, animal_eating):
    animal = Animal(animal_name)
    assert animal.eat() == animal_eating


def test_no_dog_name():
    dog = Dog()
    assert dog._name == "Rax"


def test_dog_sound():
    dog = Dog()
    assert dog.sound() == "Bark"


def test_no_cat_name():
    cat = Cat()
    assert cat._name == "Stormy"


def test_cat_sound():
    cat = Cat()
    assert cat.sound() == "Meow"


@pytest.mark.parametrize(
    "pet",
    ["Cat", "Dog", "Animal", Home()],
)
def test_if_pet_is_animal(pet):
    home = Home()
    with pytest.raises(TypeError, match="pet must be an instance of the Animal class."):
        home.adopt_pet(pet)


@pytest.mark.parametrize(
    "pet",
    [
        Dog(),
        Cat(),
        Dog("Fluffy"),
        Cat("Daisy"),
    ],
)
def test_if_pet_gets_adopted(pet):
    home = Home()
    home.adopt_pet(pet)
    assert pet in home.adopted_pets


@pytest.mark.parametrize(
    "pet",
    [
        Dog(),
        Cat(),
        Dog("Fluffy"),
        Cat("Daisy"),
    ],
)
def test_if_pet_is_already_adopted(pet):
    home = Home()
    home.adopt_pet(pet)
    with pytest.raises(ValueError, match="You cannot adopt the same pet twice."):
        home.adopt_pet(pet)


@pytest.mark.parametrize(
    "pets, pet_count",
    [
        ([Cat(), Dog()], 2),
        ([Dog(), Cat(), Dog("Johnny boy")], 3),
        ([Cat("Lilly")], 1),
    ],
)
def test_adopted_pets_count(pets, pet_count):
    home = Home()

    for pet in pets:
        assert home.adopt_pet(pet) == len(home.adopted_pets)
    assert len(home.adopted_pets) == pet_count


@pytest.mark.parametrize(
    "pets, pet_sounds",
    [
        ([Cat(), Dog()], ["Meow", "Bark"]),
        ([Dog(), Cat(), Dog("Johnny boy")], ["Bark", "Meow", "Bark"]),
        ([Cat("Lilly")], ["Meow"]),
    ],
)
def test_all_pet_sounds(pets, pet_sounds):
    home = Home()

    for pet in pets:
        home.adopt_pet(pet)
    assert home.make_all_sounds() == pet_sounds
