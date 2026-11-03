import math
import unittest
from scripts.estimate_g import estimate


class EstimatorTests(unittest.TestCase):
    def test_known_synthetic_value(self):
        g = 6.67430e-11
        rows = [{"torque_Nm": g * k, "geometry_factor": k,
                 "torque_unc_Nm": 1e-13} for k in (0.01, -0.02, 0.03)]
        result = estimate(rows)
        self.assertTrue(math.isclose(result["G_estimate_SI"], g, rel_tol=1e-12))
        self.assertEqual(result["n"], 3)

    def test_unidentifiable(self):
        with self.assertRaises(ValueError):
            estimate([{"torque_Nm": 0, "geometry_factor": 0, "torque_unc_Nm": 1}])

    def test_invalid_uncertainty(self):
        with self.assertRaises(ValueError):
            estimate([{"torque_Nm": 1, "geometry_factor": 1, "torque_unc_Nm": 0}])


if __name__ == "__main__":
    unittest.main()
