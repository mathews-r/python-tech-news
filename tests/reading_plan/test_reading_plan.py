from tech_news.analyzer.reading_plan import ReadingPlanService  # noqa: F401, E261, E501


def test_reading_plan_group_news():
    reading = ReadingPlanService()

    expect = reading.group_news_for_available_time(10)
    response = "xablau"

    assert expect == response
