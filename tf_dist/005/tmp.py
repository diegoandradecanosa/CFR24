ones = dtensor.call_with_layout(
    tf.function(tf.random.stateless_normal),
    dtensor.Layout(['x', 'y'], mesh),
    shape=(6, 4),
    seed=(1, 1))
print(ones)