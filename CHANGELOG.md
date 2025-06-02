# Changelog

All notable changes to this project will be documented in this file. 

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/), and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

_Note: 'Unreleased' section below is used for untagged changes that will be issued with the next version bump_

### [Unreleased] - 2022-00-00 
#### Added
#### Changed
#### Deprecated
#### Removed
#### Fixed
#### Security
__BEGIN-CHANGELOG__
 
### [1.1.2] - 2025-06-02
#### Changed
 - Loosen loguru reqs
 
### [1.1.1] - 2025-06-02
#### Added
 - Loosened pinned versions (yikes -- this is a library)
 - Tested in py312, likely need to more thoroughly test later
 
### [1.0.1] - 2022-04-24
#### Added
 - More type hints (albeit they'll need to be made more precise later)
 - `PyYAML` was left out of requirements upon scanning the older `setup.py` file, so that was added & pinned
#### Changed
 - `print` statements are now log outputs
 - Some dictionaries were simplified and optimized
#### Fixed
 - Minor variable misspellings
 - `test_camera.py` now doesn't test a real camera connection
 
### [1.0.0] - 2022-04-23
#### Added
 - `CHANGELOG.md`
 - Python 3.10 support
 - `tox` support
 - PPM scripts for easier package support routines

__END-CHANGELOG__