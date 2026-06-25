"""
Tests for ideation-validate module.
"""

import pytest
from ideation_validate import ProblemSignal, SignalAggregator, get_mock_signals


def test_problem_signal_creation():
    """Test that a ProblemSignal is created with correct attributes."""
    signal = ProblemSignal(
        revenue_potential=1000,
        title="Test Title",
        description="Test Desc",
        revenue_evidence="Test Evidence",
        market_size=500
    )
    assert signal.title == "Test Title"
    assert signal.revenue_potential == 1000
    assert signal.market_size == 500


def test_signal_sorting():
    """Test that SignalAggregator sorts signals by revenue potential descending."""
    # Create unsorted list
    low = ProblemSignal(100, "Low", "", "", 0)
    high = ProblemSignal(9000, "High", "", "", 0)
    mid = ProblemSignal(500, "Mid", "", "", 0)

    aggregator = SignalAggregator([low, high, mid])
    
    # Verify order
    assert aggregator.signals[0].revenue_potential == 9000
    assert aggregator.signals[1].revenue_potential == 500
    assert aggregator.signals[2].revenue_potential == 100


def test_pagination_happy_path():
    """Test standard pagination behavior."""
    signals = get_mock_signals()
    aggregator = SignalAggregator(signals)

    # Page 1
    page1 = aggregator.get_signals(page=1, page_size=2)
    assert len(page1) == 2
    # Verify they are the highest potential ones
    assert page1[0].revenue_potential >= page1[1].revenue_potential

    # Page 2
    page2 = aggregator.get_signals(page=2, page_size=2)
    assert len(page2) == 2
    # Verify page 2 items are different from page 1
    assert page1[0].title != page2[0].title


def test_pagination_out_of_bounds():
    """Test requesting a page beyond available data returns empty list."""
    signals = get_mock_signals()
    aggregator = SignalAggregator(signals)
    
    # Request a page that definitely doesn't exist
    result = aggregator.get_signals(page=999, page_size=10)
    assert result == []


def test_pagination_edge_case_exact_boundary():
    """Test pagination when page size divides total count exactly."""
    custom_signals = [
        ProblemSignal(i, f"Sig {i}", "", "", 0) for i in range(10, 0, -1)
    ]
    aggregator = SignalAggregator(custom_signals)
    
    # Total 10 items, page size 5
    page1 = aggregator.get_signals(1, 5)
    page2 = aggregator.get_signals(2, 5)
    page3 = aggregator.get_signals(3, 5)

    assert len(page1) == 5
    assert len(page2) == 5
    assert len(page3) == 0


def test_invalid_page_parameters():
    """Test that invalid page parameters raise ValueError."""
    aggregator = SignalAggregator([])

    with pytest.raises(ValueError):
        aggregator.get_signals(page=0, page_size=5)

    with pytest.raises(ValueError):
        aggregator.get_signals(page=1, page_size=0)
        
    with pytest.raises(ValueError):
        aggregator.get_signals(page=-5, page_size=10)


def test_aggregator_count():
    """Test that count returns the correct number of signals."""
    signals = get_mock_signals()
    aggregator = SignalAggregator(signals)
    assert aggregator.count() == len(signals)
