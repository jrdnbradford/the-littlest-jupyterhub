"""
Unit test functions to test JSON Schema validation
"""

import jsonschema
from tljh.config_schema import config_schema

def test_valid_json_schema():
  validator_class = jsonschema.validators.validator_for(config_schema)
  validator_class.check_schema(config_schema)
