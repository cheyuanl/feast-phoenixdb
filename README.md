# Feast Custom Online Store
[![test_phoenixdb_online_store](https://github.com/cheyuanl/feast-phoenixdb/actions/workflows/test_phoenixdb_online_store.yml/badge.svg?branch=main)](https://github.com/cheyuanl/feast-phoenixdb/actions/workflows/test_phoenixdb_online_store.yml)

### Overview

This repository implements Feast online store plugin for PhoenixDB. 

### Testing the online store in this repository

Run the following commands to test PhoenixDB online store ([PhoenixDBOnlineStore](https://github.com/cheyuanl/feast-phoenixdb/blob/master/feast_phoenixdb_online_store/phoenixdb_online_store.py))

```bash
pip install -r requirements.txt
```

```
pytest test_phoenixdb_online_store.py
```

It is also possible to run a Feast CLI command, which interacts with the online store. It may be necessary to add the 
`PYTHONPATH` to the path where your online store module is stored.
```
PYTHONPATH=$PYTHONPATH:/$(pwd) feast -c basic_feature_repo apply

```
```
Registered entity driver_id
Registered feature view driver_hourly_stats
Deploying infrastructure for driver_hourly_stats
```

```
$ PYTHONPATH=$PYTHONPATH:/$(pwd) feast -c feature_repo materialize-incremental 2021-08-19T22:29:28
```

```
Materializing 1 feature views to 2021-08-19 15:29:28-07:00 into the feast_phoenixdb_online_store.phoenixdb_online_store.PhoenixDBOnlineStore online store.

driver_hourly_stats from 2020-08-24 05:23:49-07:00 to 2021-08-19 15:29:28-07:00:
100%|████████████████████████████████████████████████████████████████| 5/5 [00:00<00:00, 120.59it/s]
```

### Testing against the Feast test suite

A subset of the Feast test suite, called "universal tests", are designed to test the core behavior of offline and online stores. A custom online store implementation can use the universal tests as follows.

First, this repository contains Feast as a submodule. To fetch and populate the directory, run
```
git submodule update --init --recursive
```

Next, install Feast following the instructions [here](https://github.com/feast-dev/feast/blob/master/CONTRIBUTING.md)
```
cd feast
pip install -e "sdk/python[ci]"
```
and confirm that the Feast unit tests run as expected:
```
make test
```

The Feast universal tests can be run with the command
```
make test-python-universal
```

If the command is run immediately, the tests should fail. The tests are parametrized based on the `FULL_REPO_CONFIGS` variable defined in `sdk/python/tests/integration/feature_repos/repo_configuration.py`. To overwrite these configurations, you can simply create your own file that contains a `FULL_REPO_CONFIGS`, and point Feast to that file by setting the environment variable `FULL_REPO_CONFIGS_MODULE` to point to that file. In this repo, the file that overwrites `FULL_REPO_CONFIGS` is `feast_phoenixdb_online_store/feast_tests.py`, so you would run
```
export FULL_REPO_CONFIGS_MODULE='feast_phoenixdb_online_store.feast_tests'
make test-python-universal
```
to test the PhoenixDB online store against the Feast universal tests. You should notice that some of the tests actually fail; this indicates that there is a mistake in the implementation of this online store!