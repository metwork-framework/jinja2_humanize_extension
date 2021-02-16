# jinja2_humanize_extension

[//]: # (automatically generated from https://github.com/metwork-framework/github_organization_management/blob/master/common_files/README.md)

**Status (master branch)**



[![GitHub CI](https://github.com/metwork-framework/jinja2_humanize_extension/workflows/CI/badge.svg?branch=master)](https://github.com/metwork-framework/jinja2_humanize_extension/actions?query=workflow%3ACI&branch=master)
[![Maintenance](https://raw.githubusercontent.com/metwork-framework/resources/master/badges/maintained.svg)](https://github.com/metwork-framework/resources/blob/master/badges/maintained.svg)




Traceback (most recent call last):
  File "/usr/local/bin/envtpl", line 11, in <module>
    load_entry_point('envtpl==0.5.3', 'console_scripts', 'envtpl')()
  File "/usr/local/lib/python3.6/dist-packages/envtpl.py", line 86, in main
    jinja2_extensions)
  File "/usr/local/lib/python3.6/dist-packages/envtpl.py", line 124, in process_file
    jinja2_extensions=jinja2_extensions)
  File "/usr/local/lib/python3.6/dist-packages/envtpl.py", line 182, in _render_string
    jinja2_extensions=jinja2_extensions)
  File "/usr/local/lib/python3.6/dist-packages/envtpl.py", line 228, in _render
    template = env.get_template(template_name)
  File "/usr/lib/python3/dist-packages/jinja2/environment.py", line 830, in get_template
    return self._load_template(name, self.make_globals(globals))
  File "/usr/lib/python3/dist-packages/jinja2/environment.py", line 804, in _load_template
    template = self.loader.load(self, name, globals)
  File "/usr/lib/python3/dist-packages/jinja2/loaders.py", line 405, in load
    return loader.load(environment, name, globals)
  File "/usr/lib/python3/dist-packages/jinja2/loaders.py", line 125, in load
    code = environment.compile(source, name, filename)
  File "/usr/lib/python3/dist-packages/jinja2/environment.py", line 591, in compile
    self.handle_exception(exc_info, source_hint=source_hint)
  File "/usr/lib/python3/dist-packages/jinja2/environment.py", line 780, in handle_exception
    reraise(exc_type, exc_value, tb)
  File "/usr/lib/python3/dist-packages/jinja2/_compat.py", line 37, in reraise
    raise value.with_traceback(tb)
  File "<unknown>", line 40, in template
  File "/usr/lib/python3/dist-packages/jinja2/environment.py", line 543, in _generate
    optimized=self.optimized)
  File "/usr/lib/python3/dist-packages/jinja2/compiler.py", line 82, in generate
    generator.visit(node)
  File "/usr/lib/python3/dist-packages/jinja2/visitor.py", line 38, in visit
    return f(node, *args, **kwargs)
  File "/usr/lib/python3/dist-packages/jinja2/compiler.py", line 754, in visit_Template
    self.blockvisit(node.body, frame)
  File "/usr/lib/python3/dist-packages/jinja2/compiler.py", line 378, in blockvisit
    self.visit(node, frame)
  File "/usr/lib/python3/dist-packages/jinja2/visitor.py", line 38, in visit
    return f(node, *args, **kwargs)
  File "/usr/lib/python3/dist-packages/jinja2/compiler.py", line 1358, in visit_Output
    self.visit(argument, frame)
  File "/usr/lib/python3/dist-packages/jinja2/visitor.py", line 38, in visit
    return f(node, *args, **kwargs)
  File "/usr/lib/python3/dist-packages/jinja2/compiler.py", line 70, in new_func
    return f(self, node, frame, **kwargs)
  File "/usr/lib/python3/dist-packages/jinja2/compiler.py", line 1578, in visit_Filter
    self.fail('no filter named %r' % node.name, node.lineno)
  File "/usr/lib/python3/dist-packages/jinja2/compiler.py", line 315, in fail
    raise TemplateAssertionError(msg, lineno, self.name, self.filename)
jinja2.exceptions.TemplateAssertionError: no filter named 'humanize_naturalsize'






## Contributing guide

See [CONTRIBUTING.md](CONTRIBUTING.md) file.



## Code of Conduct

See [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md) file.



## Sponsors

*(If you are officially paid to work on MetWork Framework, please contact us to add your company logo here!)*

[![logo](https://raw.githubusercontent.com/metwork-framework/resources/master/sponsors/meteofrance-small.jpeg)](http://www.meteofrance.com)
