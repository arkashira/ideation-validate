import json
from dataclasses import dataclass
from datetime import datetime

@dataclass
class Idea:
    id: int
    category: str
    success: bool = False
    failure: bool = False

class IdeationValidate:
    def __init__(self):
        self.ideas = []
        self.market_signals = {}

    def add_idea(self, idea):
        self.ideas.append(idea)

    def log_feedback(self, idea_id, feedback):
        for idea in self.ideas:
            if idea.id == idea_id:
                if feedback == 'Success':
                    idea.success = True
                elif feedback == 'Failure':
                    idea.failure = True
                self.market_signals[idea_id] = feedback
                break

    def show_success_rate_trends(self):
        trends = {}
        for idea in self.ideas:
            if idea.category not in trends:
                trends[idea.category] = {'success': 0, 'total': 0}
            trends[idea.category]['total'] += 1
            if idea.success:
                trends[idea.category]['success'] += 1
        return {category: values['success'] / values['total'] if values['total'] > 0 else 0 for category, values in trends.items()}

    def get_market_signals(self):
        return self.market_signals
