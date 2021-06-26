fastapi-sample
==============

Sample server program using FastAPI.


How to use
----------

Install dependencies. ::

$ poetry install

Run your sample server. ::

$ poetry run poe start

Test, format, lint your code. ::

$ poetry run poe test
$ poetry run poe fmt
$ poetry run poe lint


Use with `docker-buildenv <https://github.com/anyakichi/docker-buildenv>`_
--------------------------------------------------------------------------

Build, run or other operations from a container.  ::

  $ mkdir fastapi-sample-1 && cd $_
  $ din anyakichi/fastapi-sample-builder
  builder@fastapi-sample-1:/build$ extract
  builder@fastapi-sample-1:/build$ build
  builder@fastapi-sample-1:/build$ run
  builder@fastapi-sample-1:/build$ setup
  builder@fastapi-sample-1:/build/fastapi-sample$ poetry poe test
  builder@fastapi-sample-1:/build/fastapi-sample$ poetry poe fmt
  builder@fastapi-sample-1:/build/fastapi-sample$ poetry poe lint

Or from your host machine. ::

  $ din anyakichi/fastapi-sample-builder extract
  $ cd fastapi-sample
  $ din anyakichi/fastapi-sample-builder build
  $ din anyakichi/fastapi-sample-builder run
  $ din anyakichi/fastapi-sample-builder poetry poe test
  $ din anyakichi/fastapi-sample-builder poetry poe fmt
  $ din anyakichi/fastapi-sample-builder poetry poe lint
