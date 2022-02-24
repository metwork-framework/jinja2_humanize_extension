from jinja2.ext import Extension
from humanize import naturalsize

from humanize.time import (
    naturaldate,
    naturalday,
    naturaldelta,
    naturaltime,
    precisedelta,
)
from humanize.number import intword


try:
    from jinja2 import pass_eval_context as eval_context
except ImportError:
    from jinja2 import evalcontextfilter as eval_context


@eval_context
def humanize_intword(eval_ctx, value, format="%.1f"):
    return intword(value, format=format)


@eval_context
def humanize_naturalsize(eval_ctx, value, binary=False, gnu=False, format="%.1f"):
    return naturalsize(value, binary=binary, gnu=gnu, format=format)


@eval_context
def humanize_naturaldate(eval_ctx, value):
    return naturaldate(value)


@eval_context
def humanize_naturalday(eval_ctx, value):
    return naturalday(value)


@eval_context
def humanize_naturaldelta(
    eval_ctx, value, months=True, minimum_unit="seconds"):
    return naturaldelta(value, months=months, minimum_unit=minimum_unit, when=when)


@eval_context
def humanize_naturaltime(
    eval_ctx, value, future=False, months=True, minimum_unit="seconds", when=None
):
    return naturaltime(
        value, future=future, months=months, minimum_unit=minimum_unit, when=when
    )


@eval_context
def humanize_precisedelta(
    eval_ctx, value, minimum_unit="seconds", suppress=(), format="%0.2f"
):
    return precisedelta(
        value, minimum_unit=minimum_unit, suppress=suppress, format=format
    )


class HumanizeExtension(Extension):
    def __init__(self, environment):
        super(HumanizeExtension, self).__init__(environment)
        environment.filters["humanize_naturalsize"] = humanize_naturalsize
        environment.filters["humanize_naturaldate"] = humanize_naturaldate
        environment.filters["humanize_naturalday"] = humanize_naturalday
        environment.filters["humanize_naturaldelta"] = humanize_naturaldelta
        environment.filters["humanize_naturaltime"] = humanize_naturaltime
        environment.filters["humanize_precisedelta"] = humanize_precisedelta
        environment.filters["humanize_intword"] = humanize_intword
