# Template

This repo will serve as a template for my version of flask apps, 
because I keep repeating the same set up and making the 
same apps out of this base image.

## Project Plan

This is somewhat ordered. Plan laid out below --->

### Ordered Phases

1. Create initial template flask app (clean up still needed)
2. Script to copy/init a fresh repo
3. Script to rename the duplicated new template project/repo
4. Install `filmstock` as a python module
5. Backport this to existing projects

### Checklist

- [ ] Create initial template flask app
  - [ ] Clean up
  - [ ] Get a sample version running locally, with instructions
  - [ ] Edit Dockerfile for sample app
  - [ ] Edit GitHub Actions to build the template in a separate action as a test (possibly as a new action in addition to existing ones)
  - [ ] Look into sample app unit tests
- [ ] Script to copy/init a fresh repo
  - [ ] Make a list of all things needed for a barebones flask app
  - [ ] Copy `filmstock/app`
  - [ ] Copy the .dotfiles
  - [ ] Update any configs
- [ ] Script to rename the duplicated new template project/repo
  - [ ] Find all places that need a rename
  - [ ] Tests (unit or integration) for this script
  - [ ] Update GitHub Actions
- [ ] Install `filmstock` as a python module
- [ ] Backport this to existing projects

## Features/Ideas

- [x] Template app
- [ ] Unit tests
- [ ] Optionally include `jwt`
- [ ] Client lib (cli and python module)
- [ ] Install as python module?
- [ ] MQTT support
- [ ] Renaming script
- [ ] DB support?
- [ ] Should I have a `BaseModel` like in other projects?
- [ ] Gunicorn scripts to run
- [ ] Example `supervisor` conf scripts
- [ ] Example populate data scripts
