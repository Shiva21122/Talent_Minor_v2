"""Starter unit tests - add more as you improve the matching logic."""
from talentminer.matching.matcher import calculate_match


def test_full_match():
    score, matched, missing = calculate_match(["python", "sql"], {"python": 2, "sql": 1})
    assert score == 100.0
    assert missing == []


def test_weighted_partial_match():
    score, matched, missing = calculate_match(["python"], {"python": 3, "sql": 1})
    assert score == 75.0
    assert matched == ["python"] and missing == ["sql"]


def test_no_job_skills_returns_zero():
    score, _, _ = calculate_match(["python"], {})
    assert score == 0.0
