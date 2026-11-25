from jinja2 import Template, Environment
import datetime

def test_no_extension():
    template = Template('foo {{ bar }}')
    result = template.render(bar="foo")
    assert result == "foo foo"


def test_extension1():
    env = Environment(extensions=["jinja2_humanize_extension.HumanizeExtension"])
    template = env.from_string("test {{ \"3000000\"|humanize_naturalsize() }}")
    result = template.render()
    assert result == "test 3.0 MB"

def test_naturalday():
    env = Environment(extensions=["jinja2_humanize_extension.HumanizeExtension"])
    template = env.from_string('{{ value|humanize_naturalday(format="%Y") }}')
    result = template.render(value=datetime.date(2000, 1, 2))
    assert result == "2000"
