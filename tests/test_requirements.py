from pathlib import Path

import pkg_resources

from tests.interfaces.test_basic import BasicTests

_REQUIREMENTS_PATH = Path(__file__).parent.with_name("requirements.txt")


class RequirementTests(BasicTests):
    def test_requirements(self):
        requirements = pkg_resources.parse_requirements(_REQUIREMENTS_PATH.open())
        for requirement in requirements:
            requirement = str(requirement)
            with self.subTest(requirement=requirement):
                pkg_resources.require(requirement)
