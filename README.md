# jinja2_humanize_extension

[//]: # (automatically generated from https://github.com/metwork-framework/github_organization_management/blob/master/common_files/README.md)

**Status (master branch)**



[![GitHub CI](https://github.com/metwork-framework/jinja2_humanize_extension/workflows/CI/badge.svg?branch=master)](https://github.com/metwork-framework/jinja2_humanize_extension/actions?query=workflow%3ACI&branch=master)
[![Maintenance](https://raw.githubusercontent.com/metwork-framework/resources/master/badges/maintained.svg)](https://github.com/metwork-framework/resources/blob/master/badges/maintained.svg)




## What is it ?

This is a [jinja2](http://jinja.pocoo.org/) extension to use [humanize](https://python-humanize.readthedocs.io/) library inside jinja2 templates.

## Syntax

The generic syntax is `{{ 'VALUE'|humanize_{humanize_fn}([humanize_fn_args]) }}`.

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

The file size is: {{ 30000000|humanize_naturalsize(binary=False, gnu=True) }}

```

## Full example

```python

from jinja2 import Template, Environment

# We load the extension in a jinja2 Environment
env = Environment(extensions=["jinja2_humanize_extension.HumanizeExtension"])

template = env.from_string("The file size is : {{ 30000000|humanize_naturalsize() }}")
result = template.render()

# [...]
```






## Contributing guide

See [CONTRIBUTING.md](CONTRIBUTING.md) file.



## Code of Conduct

See [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md) file.



## Sponsors

*(If you are officially paid to work on MetWork Framework, please contact us to add your company logo here!)*

[![logo](https://raw.githubusercontent.com/metwork-framework/resources/master/sponsors/meteofrance-small.jpeg)](http://www.meteofrance.com)
