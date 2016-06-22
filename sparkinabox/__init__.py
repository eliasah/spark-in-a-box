#! /usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import (absolute_import, division, print_function)
import random
import argparse

from sparkinabox.release import __author__, __version__
from sparkinabox.makebox import make_box


def main():
    parser = argparse.ArgumentParser()

    parser.add_argument("--username", default="spark")

    parser.add_argument("--anaconda-repository", default="https://repo.continuum.io/")
    parser.add_argument("--anaconda", choices=["anaconda", "miniconda"], default="miniconda")

    parser.add_argument("--python", choices=["2", "3"], default="3")
    parser.add_argument("--python-packages", nargs="*",
                        default="numpy scipy scikit-learn numexpr numba curl toolz dask")

    parser.add_argument('--with-mkl', dest='nomkl', action="store_false")
    parser.add_argument('--no-mkl', dest='nomkl', action="store_true")
    parser.set_defaults(nomkl=True)

    parser.add_argument("--python-hashseed", default=random.randint(0, 2 ** 31 - 1), type=int)

    parser.add_argument("--scala", choices=["2.10", "2.11"], default="2.11")
    parser.add_argument("--spark", choices=["1.6.1", "2.0.0-preview"], default="2.0.0-preview")
    parser.add_argument("--jdk", choices=["7", "8"], default="8"),

    parser.add_argument("--hadoop-version", default="2.7.2")

    parser.add_argument("--with-hadoop-provided", dest="with_hadoop_provided", action="store_true")
    parser.add_argument("--no-hadoop-provided", dest="with_hadoop_provided", action="store_false")
    parser.set_defaults(hadoop_provided=True)

    parser.add_argument("--with-hive", dest="with_hive", action="store_true")
    parser.add_argument("--no-hive", dest="with_hive", action="store_false")
    parser.set_defaults(with_hive=True)

    parser.add_argument("--with-yarn", dest="with_yarn", action="store_true")
    parser.add_argument("--no-yarn", dest="with_yarn", action="store_false")
    parser.set_defaults(wiht_yarn=False)

    parser.add_argument("--with-r", dest="with_r", action="store_true")
    parser.add_argument("--no-r", dest="with_r", action="store_false")
    parser.set_defaults(with_r=False)

    parser.add_argument("--output-dir", dest="output_dir", required=True)

    parser.add_argument("--docker-prefix", dest="docker_prefix", default="zero323")
    parser.add_argument("--docker-names", dest="docker_name", default="spark-sandbox")

    parser.add_argument("--profile", choices=["local", "standalone"], default="local")
    parser.add_argument("--client-entrypoint",
                        choices=["spark-submit", "spark-shell", "pyspark", "sparkR"],
                        default="spark-submit")

    make_box(parser.parse_args())
