# jinja2_humanize_extension

[//]: # (automatically generated from https://github.com/metwork-framework/github_organization_management/blob/master/common_files/README.md)

**Status (master branch)**



[![GitHub CI](https://github.com/metwork-framework/jinja2_humanize_extension/workflows/CI/badge.svg?branch=master)](https://github.com/metwork-framework/jinja2_humanize_extension/actions?query=workflow%3ACI+branch%3Amaster)
[![Maintenance](https://raw.githubusercontent.com/metwork-framework/resources/master/badges/maintained.svg)](https://github.com/metwork-framework/resources/blob/master/badges/maintained.svg)




Traceback (most recent call last):
  File "/usr/local/bin/envtpl", line 8, in <module>
    sys.exit(main())
  File "/usr/local/lib/python3.10/dist-packages/envtpl.py", line 92, in main
    process_file(args.input_file, args.output_file, variables,
  File "/usr/local/lib/python3.10/dist-packages/envtpl.py", line 131, in process_file
    output = _render_string(stdin_read(), variables, undefined,
  File "/usr/local/lib/python3.10/dist-packages/envtpl.py", line 190, in _render_string
    return _render(template_name, loader, variables,
  File "/usr/local/lib/python3.10/dist-packages/envtpl.py", line 238, in _render
    template = env.get_template(template_name)
  File "/usr/lib/python3/dist-packages/jinja2/environment.py", line 997, in get_template
    return self._load_template(name, globals)
  File "/usr/lib/python3/dist-packages/jinja2/environment.py", line 958, in _load_template
    template = self.loader.load(self, name, self.make_globals(globals))
  File "/usr/lib/python3/dist-packages/jinja2/loaders.py", line 563, in load
    return loader.load(environment, name, globals)
  File "/usr/lib/python3/dist-packages/jinja2/loaders.py", line 137, in load
    code = environment.compile(source, name, filename)
  File "/usr/lib/python3/dist-packages/jinja2/environment.py", line 757, in compile
    self.handle_exception(source=source_hint)
  File "/usr/lib/python3/dist-packages/jinja2/environment.py", line 925, in handle_exception
    raise rewrite_traceback_stack(source=source)
  File "<unknown>", line 7, in template
jinja2.exceptions.TemplateSyntaxError: expected token 'end of print statement', got '{'






## Contributing guide

See [CONTRIBUTING.md](CONTRIBUTING.md) file.



## Code of Conduct

See [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md) file.



## Sponsors

*(If you are officially paid to work on MetWork Framework, please contact us to add your company logo here!)*

[![logo](https://raw.githubusercontent.com/metwork-framework/resources/master/sponsors/meteofrance-small.jpeg)](http://www.meteofrance.com)
