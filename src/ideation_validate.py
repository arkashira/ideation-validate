import json
import argparse
from dataclasses import dataclass

@dataclass
class Idea:
    description: str
    market_size: float
    competition_score: float
    willingness_to_pay: float

def load_model():
    # Load default model (using vLLM or SGLang)
    # For simplicity, assume a pre-trained model is available
    return lambda idea_description: Idea(idea_description, 1000.0, 0.5, 10.0)

def validate_idea(idea_description):
    model = load_model()
    idea = model(idea_description)
    return idea

def main(args=None):
    if args is None:
        parser = argparse.ArgumentParser(description='Ideation Validate')
        parser.add_argument('idea_description', nargs='?', help='Idea description')
        args = parser.parse_args()
    else:
        parser = argparse.ArgumentParser(description='Ideation Validate')
        parser.add_argument('idea_description', nargs='?', help='Idea description')
        args = parser.parse_args(args)  # Pass the list of args to parse_args

    if args.idea_description:
        idea = validate_idea(args.idea_description)
        print(json.dumps(idea.__dict__, indent=4))
    else:
        parser.print_help()

if __name__ == '__main__':
    main()
