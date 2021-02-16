## What is it ?

This is a [jinja2](http://jinja.pocoo.org/) extension to use [humanize](https://python-humanize.readthedocs.io/) library inside jinja2 templates.

## Syntax

The generic syntax is `{% raw %}{{ 'VALUE'|humanize_{humanize_fn}([humanize_fn_args]) }}{% endraw %}`.

Following [humanize](https://python-humanize.readthedocs.io/) functions are currently mapped:

- `naturalsize`
- `abs_timedelta`
- `date_and_delta`
- `naturaldate`
- `naturalday`
- `naturaldelta`
- `naturaltime`
- `precisedelta`

See [humanize](https://python-humanize.readthedocs.io/) documentation for argument details.

To take a more real example, let's take the [naturalsize()](https://python-humanize.readthedocs.io/en/latest/filesize/) function. To use it inside a [jinja2](http://jinja.pocoo.org/) template with this extension, you
have to use:

```

The file size is: {% raw %}{{ 30000000|humanize_naturalsize(binary=False, gnu=True) }}{% endraw %}

```

You can use the same logic with all supported functions. If you need other functions, feel
free to open a PullRequest.

## Installation

```
pip install jinja2-humanize-extension
```

## Full example

```python

from jinja2 import Template, Environment

# We load the extension in a jinja2 Environment
env = Environment(extensions=["jinja2_humanize_extension.HumanizeExtension"])

template = env.from_string("The file size is : {% raw %}{{ 30000000|humanize_naturalsize() }}{% endraw %}")
result = template.render()

# [...]
```
