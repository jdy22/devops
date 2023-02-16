import pytest

from literature_searcher.query_processor import process

def test_returns_empty_string_on_invalid_query():
    assert process("") == []

def test_knows_about_shakespeare():
    assert any("playwright" in result for result in process("Shakespeare"))

def test_knows_about_asimov():
    assert any("science fiction" in result for result in process("Asimov"))

def test_not_case_sensitive():
    assert any("playwwright" in result for result in process("shakespeare"))

def test_knows_about_orwell():
    assert any("novelist" in result for result in process("orwell"))

def test_knows_about_lee():
    assert any("Mockingbird" in result for result in process("lee"))

if __name__ == "__main__":
    test_returns_empty_string_on_invalid_query()
    test_knows_about_shakespeare()
    test_knows_about_asimov()
    test_not_case_sensitive()
    test_knows_about_orwell()
    test_knows_about_lee()
