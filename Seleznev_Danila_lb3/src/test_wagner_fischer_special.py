import pytest
from wagner_fischer_special import wagner_fischer_special

def test_no_special_chars():
    result = wagner_fischer_special(
        "abc", "xyz",
        replace_cost=1, insert_cost=1, delete_cost=1,
        special_replace_char='@', special_replace_cost=2,
        special_delete_char='#', special_delete_cost=2
    )
    assert result == 3

def test_special_replace_char():
    # Высокая стоимость специальной замены
    result = wagner_fischer_special(
        "a", "@",
        replace_cost=1, insert_cost=1, delete_cost=1,
        special_replace_char='@', special_replace_cost=2,
        special_delete_char='#', special_delete_cost=1
    )
    assert result == 2  # замена или удаление + вставка (одинаково)
    
    # Низкая стоимость специальной замены
    result2 = wagner_fischer_special(
        "a", "@",
        replace_cost=5, insert_cost=5, delete_cost=5,
        special_replace_char='@', special_replace_cost=1,
        special_delete_char='#', special_delete_cost=5
    )
    assert result2 == 1  # специальная замена дешевле

def test_special_delete_char():
    # Обычное удаление
    result1 = wagner_fischer_special(
        "ab", "b",
        replace_cost=2, insert_cost=2, delete_cost=1,
        special_replace_char='@', special_replace_cost=2,
        special_delete_char='#', special_delete_cost=3
    )
    assert result1 == 1  # обычное удаление
    
    # Специальное удаление (дороже обычного)
    result2 = wagner_fischer_special(
        "#b", "b",
        replace_cost=2, insert_cost=2, delete_cost=1,
        special_replace_char='@', special_replace_cost=2,
        special_delete_char='#', special_delete_cost=3
    )
    assert result2 == 3  # специальное удаление

def test_cheap_special_delete():
    result = wagner_fischer_special(
        "###", "",
        replace_cost=5, insert_cost=5, delete_cost=5,
        special_replace_char='@', special_replace_cost=5,
        special_delete_char='#', special_delete_cost=1
    )
    assert result == 3

def test_identical_strings_with_special():
    result = wagner_fischer_special(
        "#@#", "#@#",
        replace_cost=1, insert_cost=1, delete_cost=1,
        special_replace_char='@', special_replace_cost=2,
        special_delete_char='#', special_delete_cost=2
    )
    assert result == 0

