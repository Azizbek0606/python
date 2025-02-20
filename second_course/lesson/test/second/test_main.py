# from src.main import sum_ , minus_
# import pytest
# from contextlib import nullcontext as does_not_raise

# class Test_calculator:


#     @pytest.mark.parametrize(
#         'x,y,result,exception',
#         [
#             (2, 3, 5, does_not_raise()),
#             (4, 2, 6, does_not_raise()),
#             (10, -5, 5, does_not_raise()),
#             (-2, -3, -5, does_not_raise()),
#             (0, 0, 0, pytest.raises(ZeroDivisionError)),
#             (None, 5, None, pytest.raises(TypeError)),
#             (5, None, None, pytest.raises(TypeError)),
#             (None, None, None, pytest.raises(TypeError))
#         ],
#     )
#     def test__sum(x, y , result, exception):
#         with exception:
#             assert sum_(x, y) == result

#     @pytest.mark.parametrize(
#         'x,y,result,exception',
#         [
#             (2, 3, -1, does_not_raise()),
#             (4, 2, 2, does_not_raise()),
#             (10, -5, 15, does_not_raise()),
#             (-2, -3, -5, does_not_raise()),
#             (0, 0, 0, pytest.raises(ZeroDivisionError)),
#             (None, 5, None, pytest.raises(TypeError)),
#             (5, None, None, pytest.raises(TypeError)),
#             (None, None, None, pytest.raises(TypeError))
#         ]
#     )

#     def test__minus(x, y, result, exception):
#         with exception:
#             assert minus_(x, y) == result


def solution(num_list):
    for i in num_list:
        if num_list.count(i) >= 2:
            return True
    return False


print(solution([2, 14, 18, 22, 22]))  # True, chunki 22 ikki marta takrorlangan
print(solution([1, 2, 3, 4, 5]))  # False, chunki dublikat yo'q
