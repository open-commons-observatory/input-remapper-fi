"""mkdocs.yml must stay valid YAML for titles with colons, quotes and hash signs (this once broke a real site)."""
import jinja2, yaml

env = jinja2.Environment(loader=jinja2.FileSystemLoader("docs/templates"), keep_trailing_newline=True)
title = 'proj: "quoted" # not a comment'
text = env.get_template("mkdocs.yml.j2").render(vars={"title": title, "tagline": "a: b, c", "repo": "o/r"})
cfg = yaml.load("\n".join(l for l in text.splitlines() if "!!python" not in l), Loader=yaml.SafeLoader)
assert cfg["site_name"] == title, cfg
assert cfg["site_description"] == "a: b, c", cfg
print("mkdocs.yml quoting ok")
