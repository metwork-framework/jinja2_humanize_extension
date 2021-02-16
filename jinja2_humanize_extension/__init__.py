import jinja2
from jinja2.ext import Extension
from humanize import (
    naturalsize,
)

from humanize.time import (
    abs_timedelta,
    date_and_delta,
    naturaldate,
    naturalday,
    naturaldelta,
    naturaltime,
    precisedelta,
)


@jinja2.evalcontextfilter
def humanize_abs_timedelta(eval_ctx, delta):
    return abs_timedelta(delta)


@jinja2.evalcontextfilter
def humanize_naturalsize(eval_ctx, value, binary=False, gnu=False, format="%.1f"):
    return naturalsize(value, binary=binary, gnu=gnu, format=format)


@jinja2.evalcontextfilter
def humanize_date_and_delta(eval_ctx, value, *args, now=None):
    return date_and_delta(value, *args, now=now)


@jinja2.evalcontextfilter
def humanize_naturaldate(eval_ctx, value):
    return naturaldate(value)


@jinja2.evalcontextfilter
def humanize_naturalday(eval_ctx, value):
    return naturalday(value)


@jinja2.evalcontextfilter
def humanize_naturaldelta(
    eval_ctx, value, months=True, minimum_unit="seconds", when=None
):
    return naturaldelta(value, months=months, minimum_unit=minimum_unit, when=when)


@jinja2.evalcontextfilter
def humanize_naturaltime(
    eval_ctx, value, future=False, months=True, minimum_unit="seconds", when=None
):
    return naturaltime(
        value, future=future, months=months, minimum_unit=minimum_unit, when=when
    )


@jinja2.evalcontextfilter
def humanize_precisedelta(
    eval_ctx, value, minimum_unit="seconds", suppress=(), format="%0.2f"
):
    return precisedelta(
        value, minimum_unit=minimum_unit, suppress=suppress, format=format
    )


class HumanizeExtension(Extension):
    def __init__(self, environment):
        super(HumanizeExtension, self).__init__(environment)
        environment.filters["humanize_abs_timedelta"] = humanize_abs_timedelta
        environment.filters["humanize_naturalsize"] = humanize_naturalsize
        environment.filters["humanize_date_and_delta"] = humanize_date_and_delta
        environment.filters["humanize_naturaldate"] = humanize_naturaldate
        environment.filters["humanize_naturalday"] = humanize_naturalday
        environment.filters["humanize_naturaldelta"] = humanize_naturaldelta
        environment.filters["humanize_naturaltime"] = humanize_naturaltime
        environment.filters["humanize_precisedelta"] = humanize_precisedelta
