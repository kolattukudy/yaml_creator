# yaml_creator
given the files in an directory, it parses the directory find the checksum for each file and write it into a yaml structure. The final out put 
will be in the format.

```
example
- auth:
      type: s3
      id: falkonry
      region: us-west-2
    filename: lxml-4.8.0-cp37-cp37m-manylinux_2_17_x86_64.manylinux2014_x86_64.manylinux_2_24_x86_64.whl
    url: "s3://falkonry-platform-one-dev/lxml-4.8.0-cp37-cp37m-manylinux_2_17_x86_64.manylinux2014_x86_64.manylinux_2_24_x86_64.whl"
    validation:
      type: sha256
      value: fa9b7c450be85bfc6cd39f6df8c5b8cbd76b5d6fc1f69efec80203f9894b885f

  - auth:
      type: s3
      id: falkonry
      region: us-west-2
    filename: gremlinpython-3.6.0-py2.py3-none-any.whl
    url: s3://falkonry-platform-one-dev/gremlinpython-3.6.0-py2.py3-none-any.whl
    validation:
      type: sha256
      value: 79f8e5e2f0d82afe017afbf6b742ce66751ac961e1d068564e052cb7d163ea06
````
