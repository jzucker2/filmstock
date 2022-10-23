# Update Dependencies

I have a process for updating dependencies.

```
cat .python-version
rm .python-version
pyenv virtualenv 3.10.7 filmstock-example-3.10.7
pyenv virtualenv <version> <unique name>-<version>

echo "<unique name>-<version>" > .python-version
cd ..
cd filmstock
pip freeze
# should be empty, now install latest pip, according to `Dockerfile`
pip install pip==22.3
```

Now run the following, but first make sure to pin 
any dependencies that you don't want automatically 
updated.

```
pip install --upgrade -r upgrade-requirements.txt
```

Then replace the dependencies in the other files, commit, and push.