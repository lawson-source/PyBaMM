#
# Tests for the lead-acid LOQS model
#
from __future__ import absolute_import, division
from __future__ import print_function, unicode_literals
import pybamm
import tests

import unittest
import numpy as np


class TestLeadAcidLOQS(unittest.TestCase):
    def test_basic_processing(self):
        model = pybamm.lead_acid.LOQS()
        model.default_parameter_values.update({"Typical current density": 0.1})
        modeltest = tests.StandardModelTest(model)
        modeltest.test_all()

    def test_optimisations(self):
        model = pybamm.lead_acid.LOQS()
        optimtest = tests.OptimisationsTest(model)

        original = optimtest.evaluate_model()
        simplified = optimtest.evaluate_model(simplify=True)
        using_known_evals = optimtest.evaluate_model(use_known_evals=True)
        simp_and_known = optimtest.evaluate_model(simplify=True, use_known_evals=True)
        np.testing.assert_array_almost_equal(original, simplified)
        np.testing.assert_array_almost_equal(original, using_known_evals)
        np.testing.assert_array_almost_equal(original, simp_and_known)

    # def test_charge(self):
    #     model = pybamm.lead_acid.LOQS()
    #     parameter_values = model.default_parameter_values
    #     parameter_values.update({"Typical current density": -1})
    #     modeltest = tests.StandardModelTest(model, parameter_values=parameter_values)
    #     modeltest.test_all()
    #
    # def test_zero_current(self):
    #     model = pybamm.lead_acid.LOQS()
    #     parameter_values = model.default_parameter_values
    #     parameter_values.update({"Typical current density": 0})
    #     modeltest = tests.StandardModelTest(model, parameter_values=parameter_values)
    #     modeltest.test_all()


if __name__ == "__main__":
    print("Add -v for more debug output")
    import sys

    if "-v" in sys.argv:
        debug = True
    unittest.main()
