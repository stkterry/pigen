#!/usr/bin/env python

"""Tests for `pigen` package."""

import unittest
import pigen
import os

DIGITS = open(f'{os.getcwd()}/tests/1K_digits_of_pi.txt', 'r').read()
NUM = len(DIGITS)


class TestPigen(unittest.TestCase):
  """Tests for generators"""

  def test_000_spigot(self):
    print('Check that the spigot generator returns correct digits.')
    pi_gen = pigen.spigot_pi()
    digits = "".join([str(next(pi_gen)) for n in range(NUM)])
    self.assertEqual(digits, DIGITS)

  def test_001_frac(self):
    print('Check that the frac generator returns correct digits.')
    pi_gen = pigen.frac_pi()
    digits = "".join([str(next(pi_gen)) for n in range(NUM)])
    self.assertEqual(digits, DIGITS)

  def test_002_chudnovsky(self):
    print('Check that Chudnovsky returns correct digits.')
    digits = str(pigen.chudnovsky_pi(NUM - 1))
    self.assertEqual(digits, DIGITS)
