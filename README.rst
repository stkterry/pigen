===================================================
PiGen : Generators For Digits of Pi
===================================================


.. image:: https://img.shields.io/pypi/v/pigen.svg
        :target: https://pypi.python.org/pypi/pigen

.. image:: https://img.shields.io/travis/stkterry/pigen.svg
        :target: https://travis-ci.org/stkterry/pigen

.. image:: https://readthedocs.org/projects/pigen/badge/?version=latest
        :target: https://pigen.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status


Overview
--------
A small collection of generators and functions for digits of pi. Maybe 
you've an art or math project and need to generate a few thousand to
a few million digits of pi?  This will help with that.


Generators
----------

Spigot's Algorithm | *pigen.spigot_pi*
======================================

* spigot_pi is a generator function.
* Useful when you only need a single digit at a time.
* Not as fast as frac_pi but a classic...

.. code-block:: python

  from pigen import spigot_pi as spi

  pi_gen = spi()
  for _ in range(100): # Let's iterate through the first 100 digits of pi.
    digit = next(pi_gen)
    # do something with digit

Fractional Continuation | *pigen.frac_pi*
=========================================

* frac_pi is a generator function.
* Useful when you only need a single digit at a time.
* Fastest single digit generator currently in the package.
* You can pass your own lambda functions for other well behaved irrational numbers!
* You can specify the base for output as well, i.e., decimal, hex, etc.

.. code-block:: python

  from pigen import frac_pi as fpi

  pi_gen = fpi()
  for _ in range(100): # Let's iterate through the first 100 digits of pi.
    digit = next(pi_gen)
    # do something with digit

  # We can pass lambdas to get different transcendental numbers.
  # The golden ratio
  phi_gen = fpi(lambda a: 1, lambda b: 1, base=10)
  for _ in range(1000): # Let's iterate through the first 1000 digits of phi.
    digit = next(phi_gen)
    # do something with digit


Chudnovsky's Pure Algorithm | *pigen.chudnovsky_pi*
===================================================

* chudnovsky_pi is a regular function.
* Useful if you need many digits at once.
* Slower than using pigen.frac_pi but less fussy.
* You need only pass the number of digits you'd like to generate.

.. code-block:: python

  from pigen import chudnovsky_pi as cpi
  n = 1000
  n_pi_digits = cpi(n) # An integer `n` digits long containing digits of pi
  

Chudnovsky's Binary Search | *pigen.chudnovsky_pi_bs*
=====================================================

* chudnovsky_pi_bs is a regular function.
* Useful if you need many digits at once.
* The absolute fastest across the board. If you need a million
* digits or more, this has got you covered.
* You need only pass the number of digits you'd like to generate.
* Makes heavy use of gmpy2 and the associated libs.  Very fast but you may need to install other platform specific dependencies.

.. code-block:: python
 
  from pigen import chudnovsky_pi_bs as cpibs
  n = 1000000
  n_pi_digits = cpibs(n) # An integer `n` digits long containing digits of pi
  
Other
-----
* Free software: MIT license

* TODO

  * CLI
  * Examples

Credits
-------
* The Chudnovsky's BS Algorithm was pulled and updated from an example by Nick Craig-Wood.
