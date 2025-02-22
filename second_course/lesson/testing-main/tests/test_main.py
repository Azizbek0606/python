# from src.main import sum_, minus
import pytest
# from contextlib import nullcontext as does_not_raise


# class TestCalculator:
#     @pytest.mark.parametrize(
#         "x, y, result, expectation",
#         [
#             (1, 1, 2, does_not_raise()),
#             (1, "1", 2, pytest.raises(TypeError)),
#             (-1, -1, -2, does_not_raise()),
#             (2**65, 2**65, 2**66, does_not_raise()),
#             (1.1, 1.1, 2.2, pytest.raises(TypeError)),
#             ([1], [1], [1, 1], pytest.raises(TypeError)),
#             (1 + 3j, 1 + 5j, 2 + 8j, pytest.raises(TypeError)),
#         ],
#     )
#     def test__sum(self, x, y, result, expectation):
#         with expectation:
#             assert sum_(x, y) == result

#     @pytest.mark.parametrize(
#         "x, y, result, expectation",
#         [
#             (1, 1, 0, does_not_raise()),
#             (1, "1", 0, pytest.raises(TypeError)),
#             (-1, -1, 0, does_not_raise()),
#             (2**65, 2**65, 0, does_not_raise()),
#             (1.1, 1.1, 0, pytest.raises(TypeError)),
#             ([1], [1], 0, pytest.raises(TypeError)),
#             (1 + 3j, 1 + 5j, 0, pytest.raises(TypeError)),
#         ],
#     )
#     def test_minus(self, x, y, result, expectation):
#         with expectation:
#             assert minus(x, y) == result


def test_fixture(example_fixture):
    name = example_fixture["name"]
    assert name == "Bob"

def test_read_file(temp_file):
    assert temp_file.read_text() == "hello world"