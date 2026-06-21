from ideation_validate import IdeationValidate, Idea

def test_add_idea():
    validate = IdeationValidate()
    idea = Idea(1, 'category1')
    validate.add_idea(idea)
    assert len(validate.ideas) == 1

def test_log_feedback_success():
    validate = IdeationValidate()
    idea = Idea(1, 'category1')
    validate.add_idea(idea)
    validate.log_feedback(1, 'Success')
    assert validate.ideas[0].success

def test_log_feedback_failure():
    validate = IdeationValidate()
    idea = Idea(1, 'category1')
    validate.add_idea(idea)
    validate.log_feedback(1, 'Failure')
    assert validate.ideas[0].failure

def test_show_success_rate_trends():
    validate = IdeationValidate()
    idea1 = Idea(1, 'category1')
    idea2 = Idea(2, 'category1')
    idea3 = Idea(3, 'category2')
    validate.add_idea(idea1)
    validate.add_idea(idea2)
    validate.add_idea(idea3)
    validate.log_feedback(1, 'Success')
    validate.log_feedback(2, 'Success')
    trends = validate.show_success_rate_trends()
    assert trends['category1'] == 1.0
    assert trends['category2'] == 0.0

def test_get_market_signals():
    validate = IdeationValidate()
    idea = Idea(1, 'category1')
    validate.add_idea(idea)
    validate.log_feedback(1, 'Success')
    signals = validate.get_market_signals()
    assert signals[1] == 'Success'
