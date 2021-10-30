from pipeline import Pipeline, pipeline_function, Variable


@pipeline_function
def square(a: float) -> float:
    return a ** 2


@pipeline_function
def minus(a: float, b: float) -> float:
    return a - b


@pipeline_function
def multiply(a: float, b: float) -> float:
    return a * b


with Pipeline() as pipeline:
    flt_1 = Variable(variable_type=float, is_input=True)
    flt_2 = Variable(variable_type=float, is_input=True)

    sq_1 = square(flt_1)
    res_1 = multiply(flt_2, sq_1)
    res_2 = minus(res_1, sq_1)
    sq_2 = square(res_2)
    res_3 = multiply(flt_2, sq_2)
    res_4 = minus(res_3, sq_1)
    pipeline.output(res_2, res_4)

output_pipeline = Pipeline.get_pipeline()
print("Pipeline graph:\n%s" % output_pipeline.json())
print(pipeline.run(5.0, 6.0))
