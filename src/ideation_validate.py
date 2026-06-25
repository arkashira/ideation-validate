"""
ideation-validate: Problem Signal Aggregator

This module provides functionality to aggregate, sort, and paginate
problem signals based on revenue potential.
"""

import argparse
from dataclasses import dataclass, field
from typing import List


@dataclass(order=True)
class ProblemSignal:
    """
    Represents a single problem signal identified in the market.
    Sorted primarily by revenue_potential (descending).
    """
    revenue_potential: int  # Higher is better, used for sorting
    title: str = field(compare=False)
    description: str = field(compare=False)
    revenue_evidence: str = field(compare=False)
    market_size: int = field(compare=False)  # e.g., TAM in dollars or user count

    def __str__(self):
        return (
            f"[${self.revenue_potential:,}] {self.title}\n"
            f"  Desc: {self.description}\n"
            f"  Evidence: {self.revenue_evidence}\n"
            f"  Market Size: {self.market_size:,}"
        )


class SignalAggregator:
    """
    Manages a collection of problem signals, handling sorting and pagination.
    """

    def __init__(self, signals: List[ProblemSignal]):
        # Sort signals by revenue potential (descending) upon initialization
        self.signals = sorted(signals, key=lambda x: x.revenue_potential, reverse=True)

    def get_signals(self, page: int = 1, page_size: int = 5) -> List[ProblemSignal]:
        """
        Returns a paginated list of signals.

        Args:
            page: The page number (1-indexed).
            page_size: The number of items per page.

        Returns:
            A list of ProblemSignal objects for the requested page.
        """
        if page < 1:
            raise ValueError("Page number must be >= 1")
        if page_size < 1:
            raise ValueError("Page size must be >= 1")

        start_index = (page - 1) * page_size
        end_index = start_index + page_size

        return self.signals[start_index:end_index]

    def count(self) -> int:
        """Returns the total number of signals."""
        return len(self.signals)


def get_mock_signals() -> List[ProblemSignal]:
    """
    Generates a set of mock problem signals to simulate a database.
    """
    return [
        ProblemSignal(
            revenue_potential=5000000,
            title="API Latency Monitor for Fintech",
            description="Fintech apps lose millions to latency. Real-time alerting needed.",
            revenue_evidence="Survey of 50 CTOs: 80% would pay $500/mo for <1ms alerts.",
            market_size=12000
        ),
        ProblemSignal(
            revenue_potential=250000,
            title="AI Code Reviewer for Legacy COBOL",
            description="Banks struggle to find COBOL devs. AI can suggest refactors.",
            revenue_evidence="3 Major banks expressed interest in pilot program at $10k/mo.",
            market_size=500
        ),
        ProblemSignal(
            revenue_potential=12000000,
            title="Automated Compliance Checker for GDPR",
            description="Small SaaS apps fear GDPR fines. Automated scanning is high demand.",
            revenue_evidence="Waitlist of 200 founders willing to pay $99/mo immediately.",
            market_size=500000
        ),
        ProblemSignal(
            revenue_potential=75000,
            title="Remote Team Watercooler Bot",
            description="Isolation in remote teams lowers retention. Gamified chat bot.",
            revenue_evidence="Current competitor has $5k MRR with poor UX.",
            market_size=45000
        ),
        ProblemSignal(
            revenue_potential=890000,
            title="Supply Chain Visualizer for Coffee Shops",
            description="Coffee shops want to show origin of beans to customers.",
            revenue_evidence="Local chain agreed to pay $2k setup + $200/mo for 10 locations.",
            market_size=30000
        ),
        ProblemSignal(
            revenue_potential=150000,
            title="Instagram DM CRM for Influencers",
            description="Influencers lose business opportunities in DMs.",
            revenue_evidence="User interview: 'I would pay $50/mo to never miss a sponsorship'.",
            market_size=100000
        ),
        ProblemSignal(
            revenue_potential=4500000,
            title="Serverless Log Aggregator",
            description="Cloudwatch is expensive. Developers need a cheaper alternative.",
            revenue_evidence="HackerNews post: 500 upvotes, 'Shut up and take my money'.",
            market_size=80000
        )
    ]


def main():
    """CLI entry point to browse signals."""
    parser = argparse.ArgumentParser(description="Browse Problem Signals")
    parser.add_argument("--page", type=int, default=1, help="Page number")
    parser.add_argument("--size", type=int, default=5, help="Items per page")
    args = parser.parse_args()

    signals = get_mock_signals()
    aggregator = SignalAggregator(signals)

    print(f"--- Problem Signals (Page {args.page}) ---")
    print(f"Total Signals: {aggregator.count()}\n")

    page_signals = aggregator.get_signals(args.page, args.size)

    if not page_signals:
        print("No signals found for this page.")
    else:
        for signal in page_signals:
            print(signal)
            print("-" * 40)


if __name__ == "__main__":
    main()
