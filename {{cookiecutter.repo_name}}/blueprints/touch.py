from stacker.blueprints.base import Blueprint

from troposphere.cloudformation import WaitConditionHandle


class Touch(Blueprint):
    """Touch creates a wait condition handle and nothing else.

    For learning / functional testing.
    """

    def create_touch_wait_condition_handle(self):
        self.template.description = ("touch waits for nothing and "
                                     "returns quickly")
        self.template.add_resource(
            WaitConditionHandle("touchNothing")
        )

    def create_template(self):
        self.create_touch_wait_condition_handle()
