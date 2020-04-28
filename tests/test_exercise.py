import pytest
import src.exercise

def test_exercise():
    input_values = ["11","4","5","64","9999","4","11","5","5","64","9999","5"]
    output = []

    def mock_input(s=None):
        if s is not None:
            output.append(s)
            return input_values.pop(0)
        else:
            output.append("")
            return input_values.pop(0)

    src.exercise.input = mock_input
    src.exercise.print = lambda s : output.append(s)

    src.exercise.main()

    src.exercise.input = mock_input
    src.exercise.print = lambda s : output.append(s)

    src.exercise.main()

    assert output[0:5] == ["","","","","Smallest number: 4","Found at index: 1"]
    assert output[6:12] == ["","","","","Smallest number: 5","Found at index: 1","Found at index: 2"]
