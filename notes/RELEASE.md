# Release

Make sure to update the `version`, as explained 
in `notes/VERSION.md`.

## Instructions

Creating a tag will create the release of the base docker 
image, using [GitHub Actions.](https://github.com/features/actions)

```
git checkout master
git pull
cat filmstock/app/version.py

git tag <version> -m "<Update message>"
git tag 0.5.0 -m "Added first template sample project, along with updated docs"
git push origin 0.5.0
```
