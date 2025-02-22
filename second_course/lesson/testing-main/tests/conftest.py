import pytest
from pathlib import Path

@pytest.fixture
def example_fixture():
    return {"name": "Bob", "age": 25}


@pytest.fixture
def temp_file():
    file = Path("file.txt")
    file.write_text("hello world")
    return file
