import TaskPacket as T
import pytest

@pytest.mark.parametrize("numbers, expected", [
    ([1,2,3,4,5],25)
])

def test_operations(numbers, expected):
    assert T.three.operationsFunc(numbers) == expected

@pytest.mark.parametrize('radius, expected_area', [
    (42, 131.9469),
])

def test_area_circle(radius, expected_area):
    assert T.two.area_calc(radius) == expected_area

@pytest.mark.parametrize('point, radius, expected_status', [
    ((23, 34), 42, True),
    ((30, 30), 42, False),
])

def test_point_in_circle(point, radius, expected_status):
    assert T.two.point_in_circle(point, radius) == expected_status

@pytest.mark.parametrize("my_favorite_movies, expected_output", [
    ('Терминатор, Пятый элемент, Аватар, Чужие, Назад в будущее', "Терминатор,\nНазад в будущее,\nПятый элемент,\nЧужие."),
    ('Один дома, Интерстеллар, Властелин колец, Ишак Олег', "Один дома,\nИшак Олег,\nИнтерстеллар,\nВластелин колец."),
    ('Гарри Поттер, Звездные войны, Трансформеры, Выживание в Тамбове', "Гарри Поттер,\nВыживание в Тамбове,\nЗвездные войны,\nТрансформеры."),
])

def test_favorite_films(my_favorite_movies, expected_output):
    assert  T.four.search_films(my_favorite_movies) == expected_output

@pytest.mark.parametrize("my_family_height", [
    [['Отец', 180], ['Мать', 165], ['Я', 175], ['Брат', 185], ['Сестра', 160]],
    [['Дедушка', 170], ['Бабушка', 155], ['Отец', 180], ['Мама', 165], ['Я', 175], ['Сестра', 160], ['Брат', 185]],
    [['Дедушка', 170], ['Бабушка', 155], ['Отец', 180], ['Мама', 165], ['Я', 175], ['Сестра', 160], ['Брат', 185], ['Кузен', 170], ['Тётя', 165]]
])
def test_father_height(my_family_height):
    assert T.five.get_father_height(my_family_height) == "Рост отца - 180 см"

@pytest.mark.parametrize("my_family_height", [
    [['Отец', 180], ['Мать', 165], ['Я', 175], ['Брат', 185], ['Сестра', 160]],
])
def test_family_height(my_family_height):
    assert T.five.get_family_height(my_family_height) == "Общий рост моей семьи - "+str(865)+" см"

@pytest.mark.parametrize("zoo, expected_output", [
    (['lion', 'kangaroo', 'elephant', 'monkey'], ['lion', 'bear', 'kangaroo', 'elephant', 'monkey']),
])

def test_new_animal(zoo, expected_output):
    assert T.six.new_animal(zoo, 1, 'bear') == ['lion', 'bear', 'kangaroo', 'elephant', 'monkey']

@pytest.mark.parametrize("zoo, new_animals, expected_output", [
    (['lion', 'kangaroo', 'elephant', 'monkey'], ['rooster', 'ostrich', 'lark'], ['lion', 'kangaroo', 'elephant', 'monkey', 'rooster', 'ostrich', 'lark']),
])

def test_new_animals(zoo, new_animals, expected_output):
    assert T.six.new_animals(zoo, new_animals) == expected_output

@pytest.mark.parametrize("zoo, expected_output", [
    (['lion', 'kangaroo', 'elephant', 'monkey'], ['lion', 'kangaroo', 'monkey']),
])

def test_free_the_beast(zoo, expected_output):
    assert T.six.free_the_beast(zoo, 'elephant') == expected_output

@pytest.mark.parametrize("zoo, animal, expected_output", [
    (['lion', 'kangaroo', 'elephant', 'monkey'], 'lion', '1'),
    (['lion', 'kangaroo', 'elephant', 'monkey', 'rooster', 'ostrich', 'lark'], 'lark', '7'),
])

def test_get_animal_cage(zoo, animal, expected_output):
    assert T.six.get_animal_index_but_for_normal_peoples(zoo, animal) == zoo.index(animal)+1