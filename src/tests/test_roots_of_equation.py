import pytest

from roots_of_equation import SecondDegreeEquation


class TestMaxMin:
    @staticmethod
    def _run_get_roots(a, b, c):
        instance = SecondDegreeEquation(a, b, c)
        return instance.get_roots()

    def test_get_roots_returns_positive_roots(self):
        roots = self._run_get_roots(1, -6, 5)
        assert roots == (5.0, 1.0)

    def test_get_roots_returns_negative_roots(self):
        roots = self._run_get_roots(3, 4, 1)
        assert roots == (-0.3333333333333333, -1.0)

    def test_get_roots_returns_positive_and_negative_roots(self):
        roots = self._run_get_roots(1, -3, -10)
        assert roots == (5.0, -2.0)

    @pytest.mark.parametrize("input_, expected_output",
                             [((1, 2, 1), (-1.0, None)),
                              ((1, 4, 4), (-2.0, None))])
    def test_get_roots_returns_only_first_root(self, input_, expected_output):
        roots = self._run_get_roots(*input_)
        assert roots == expected_output

    def test_get_roots_with_delta_less_than_zero_returns_invalid_roots(self):
        instance = SecondDegreeEquation(9, 5, 4)
        assert instance.delta <= 0
        roots = instance.get_roots()
        assert roots == (None, None)

    def test_get_roots_with_a_param_being_zero_raises(self):
        with pytest.raises(ValueError):
            self._run_get_roots(0, 5, 4)
