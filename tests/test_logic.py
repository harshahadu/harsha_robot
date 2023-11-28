import pytest
from robotToyLogic import logic

def test_executeCommand_move():
    x, y, pos = 1, 1, 0  # Starting position
    command = "MOVE"
    new_x, new_y, new_pos = logic.executeCommand(x, y, pos, command)
    assert (new_x, new_y, new_pos) == (1, 2, 0)

def test_executeCommand_left():
    x, y, pos = 1, 1, 0  # Starting position
    command = "LEFT"
    new_x, new_y, new_pos = logic.executeCommand(x, y, pos, command)
    assert (new_x, new_y, new_pos) == (1, 1, 3)

def test_executeCommand_right():
    x, y, pos = 1, 1, 0  # Starting position
    command = "RIGHT"
    new_x, new_y, new_pos = logic.executeCommand(x, y, pos, command)
    assert (new_x, new_y, new_pos) == (1, 1, 1)

def test_executeCommand_boundary():
    x, y, pos = 4, 4, 0  # Starting position at the top-right corner
    command = "MOVE"
    new_x, new_y, new_pos = logic.executeCommand(x, y, pos, command)
    assert (new_x, new_y, new_pos) == (4, 4, 0)  # Should stay at the same position

def test_executeCommand_wrap_around():
    x, y, pos = 0, 0, 0  # Starting position at the bottom-left corner
    command = "LEFT"
    new_x, new_y, new_pos = logic.executeCommand(x, y, pos, command)
    assert (new_x, new_y, new_pos) == (0, 0, 3)  # Should wrap around to the right direction

def test_executeCommand_invalid_command():
    x, y, pos = 1, 1, 0  # Starting position
    command = "INVALID"
    with pytest.raises(ValueError):
        logic.executeCommand(x, y, pos, command)