import logging
import os
import pathlib
import shutil
from unittest import TestCase

from allennlp.common.checks import log_pytorch_version_info


class CustomTestCase(TestCase):
    """
    A custom subclass of :class:`~unittest.TestCase` that disables some of the
    more verbose AllenNLP logging and that creates and destroys a temp directory
    as a test fixture.
    """
    PROJECT_ROOT = (pathlib.Path(__file__).parent / ".." / "..").resolve()
    MODULE_ROOT = PROJECT_ROOT / "contexteval"
    TESTS_ROOT = PROJECT_ROOT / "tests"
    FIXTURES_ROOT = TESTS_ROOT / "fixtures"

    def setUp(self):
        logging.basicConfig(format='%(asctime)s - %(levelname)s - %(name)s - %(message)s',
                            level=logging.DEBUG)
        # Disabling some of the more verbose logging statements that typically aren't very helpful
        # in tests.
        logging.getLogger('allennlp.common.params').disabled = True
        logging.getLogger('allennlp.nn.initializers').disabled = True
        logging.getLogger('allennlp.modules.token_embedders.embedding').setLevel(logging.INFO)
        logging.getLogger('urllib3.connectionpool').disabled = True
        log_pytorch_version_info()

        self.TEST_DIR = pathlib.Path("/tmp/contexteval_tests/")

        os.makedirs(self.TEST_DIR, exist_ok=True)

    def tearDown(self):
        shutil.rmtree(self.TEST_DIR)
