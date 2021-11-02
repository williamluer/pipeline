from pipeline import Pipeline, pipeline_function, Variable


class MyClass(object):
    def __init__(self, var):
        self.var = var


@pipeline_function
def add_lol(a: str) -> MyClass:
    return MyClass(a + " lol")


with Pipeline() as pipeline:
    my_class_var = Variable(variable_type=str, is_input=True)

    output_class = add_lol(my_class_var)
    print(output_class)

    pipeline.output(output_class)


print(pipeline.run("Hey")[0].var)