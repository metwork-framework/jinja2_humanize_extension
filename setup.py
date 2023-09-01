from setuptools import setup, find_packages

with open('requirements.txt') as reqs:
    install_requires = [
        line for line in reqs.read().split('\n')
        if (line and not line.startswith('--')) and (";" not in line)]

with open("README.md") as f:
    long_description = f.read().replace("{% raw %}", "").replace("{% endraw %}", "")

setup(
    author="Fabien MARTY, Jean-Baptiste VESLIN",
    author_email="fabien.marty@gmail.com, jbaptiste31@free.fr",
    name="jinja2_humanize_extension",
    version="0.4.0",
    license="BSD",
    packages=find_packages(),
    install_requires=install_requires,
    python_requires='>=3.0',
    description="a jinja2 extension to use humanize library inside jinja2 templates",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/metwork-framework/jinja2_humanize_extension",
    keywords="jinja2 extension",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Programming Language :: Python :: 3"
    ]
)
