from math import log10
from gmpy2 import isqrt, mpz


def spigot_pi():
  """Generates digits of pi using the spigot algorithm."""
  q, r, t, k, n, ll = 1, 0, 1, 1, 3, 3
  while True:
    if 4 * q + r - t < n * t:
      yield n
      q, r, t, k, n, ll = (
          10 * q, 10 * (r - n * t), t, k,
          (10 * (3 * q + r)) // t - 10 * n, ll
      )
    else:
      q, r, t, k, n, ll = (
          q * k, (2 * q + r) * ll, t * ll, k + 1,
          (q * (7 * k + 2) + r * ll) // (t * ll), ll + 2
      )


def frac_pi(a=lambda k: 0 if k == 0 else 2 * k - 1,
            b=lambda k: 4 if k == 1 else (k - 1)**2,
            base=10):
  """Generate digits of a continued fraction a(0)+b(1)/(a(1)+b(2)/(...).

  Not just for generating digits of Pi, any `nicely` sequenced
  continued fraction can be generated using this function.

  Args:
    a: Represents a_k of a continued fraction.
    b: Represents b_k of a continued fraction.
    base: The base of the number system you wish as output,
      i.e., decimal, hex, etc.
  """
  (p0, q0), (p1, q1) = (a(0), 1), (a(1) * a(0) + b(1), a(1))
  k = 1
  while True:
    (d0, r0), (d1, r1) = divmod(p0, q0), divmod(p1, q1)
    if d0 == d1:
      yield d1
      p0, p1 = base * r0, base * r1
    else:
      k = k + 1
      x, y = a(k), b(k)
      (p0, q0), (p1, q1) = (p1, q1), (x * p1 + y * p0, x * q1 + y * q0)


def chudnovsky_pi(digits):
  """
  Compute int(pi * 10**digits)

  This is done using Chudnovsky's series with binary splitting
  """
  C = 640320
  C3 = C**3 // 24

  def binary_split(a, b):
    """
    Computes the terms for binary splitting the Chudnovsky infinite series

    a(a) = +/- (13591409 + 545140134*a)
    p(a) = (6*a-5)*(2*a-1)*(6*a-1)
    b(a) = 1
    q(a) = a*a*a*C3

    returns P(a,b), Q(a,b) and T(a,b)
    """
    if b - a == 1:

      if a == 0:  # Directly compute P(a,a+1), Q(a,a+1) and T(a,a+1)
        Pab = Qab = mpz(1)
      else:
        Pab = mpz((6 * a - 5) * (2 * a - 1) * (6 * a - 1))
        Qab = mpz(a * a * a * C3)
      Tab = Pab * (13591409 + 545140134 * a)  # a(a) * p(a)
      if a & 1:
        Tab = -Tab
    else:
      # Recursively compute P(a,b), Q(a,b) and T(a,b)
      # m is the midpoint of a and b
      m = (a + b) // 2
      # Recursively calculate P(a,m), Q(a,m) and T(a,m)
      Pam, Qam, Tam = binary_split(a, m)
      # Recursively calculate P(m,b), Q(m,b) and T(m,b)
      Pmb, Qmb, Tmb = binary_split(m, b)
      # Now combine
      Pab = Pam * Pmb
      Qab = Qam * Qmb
      Tab = Qmb * Tam + Pam * Tmb
    return Pab, Qab, Tab

  # how many terms to compute
  num_digits = log10(C3 / 6 / 2 / 6)
  N = int(digits / num_digits + 1)
  # Calculate P(0,N) and Q(0,N)
  _, Q, T = binary_split(0, N)
  one_squared = mpz(10)**(2 * digits)
  sqrtC = isqrt(10005 * one_squared)
  return (Q * 426880 * sqrtC) // T
