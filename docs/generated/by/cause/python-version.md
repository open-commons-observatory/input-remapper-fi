# cause: `python-version`

Python version incompatibility or dependency version

4 analysed items carry this tag. [Back to index](../../index.md)

| Item | State | Title | Summary |
|---|---|---|---|
| [#213](https://github.com/sezanzeb/input-remapper/issues/213) | CLOSED | Installing from release tarball with setup.py fails - "not a git repo… | CentOS 7, Python 3.6, offline: setup.py failed with "not a git repository" because commit_hash.py generation requires git. Workaround: initialize git repo first. Also: evdev C compilation issue on Py… |
| [#231](https://github.com/sezanzeb/input-remapper/issues/231) | CLOSED | After upgrading python to 3.10 Key-Mapper is not working anymore | Python 3.10 upgrade breaks key-mapper: package installed into python3.8 path not in python3.10 sys.path. Multiple reporters. Root: python version mismatch between pip/setup.py and system default. Fix… |
| [#278](https://github.com/sezanzeb/input-remapper/issues/278) | CLOSED | Checked out repo, app will not launch due to keyword argument error | App crashed with keyword argument error after checking out main branch on Ubuntu 21.10. Root: jonasBoss added `slots=True` to a dataclass which requires Python ≥3.10; Ubuntu ships 3.8. Fixed by remov… |
| [#281](https://github.com/sezanzeb/input-remapper/issues/281) | CLOSED | downgrading | pyenv Python installation: service cannot import input-remapper because pyenv paths are user-local, inaccessible by root systemd service. Root: pyenv is incompatible with root systemd services. Worka… |
