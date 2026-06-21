import pytest
from io import StringIO
import sys
from ideation_validate import validate_idea
from src import __main__

def test_validate_idea():
    idea_description = "Test idea"
    idea = validate_idea(idea_description)
    assert idea.description == idea_description
    assert idea.market_size == 1000.0
    assert idea.competition_score == 0.5
    assert idea.willingness_to_pay == 10.0

def test_main(capsys):
    idea_description = "Test idea"
    __main__.main([idea_description])  # Call main function
    captured = capsys.readouterr()
    assert "description" in captured.out
    assert "market_size" in captured.out
    assert "competition_score" in captured.out
    assert "willingness_to_pay" in captured.out
