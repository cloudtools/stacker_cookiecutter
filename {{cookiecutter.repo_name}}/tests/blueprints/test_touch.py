# reference:
#  http://stacker.readthedocs.io/en/latest/blueprints.html#testing-blueprints
#
# You should remove this and add your own tests. This is an example.

from stacker.context import Context

from stacker.blueprints.testutil import BlueprintTestCase

from blueprints.touch import Touch

class TestTouchBlueprint(BlueprintTestCase):
    def setUp(self):
        self.ctx = Context({'namespace': 'test', 'environment': 'test'})

    def test_touch(self):
        blueprint = Touch('test_touch', self.ctx)
        blueprint.create_template()
        self.assertRenderedBlueprint(blueprint)

