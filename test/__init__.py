from gwlfe.Memoization import memoize_with_args
from mock import patch

patch('gwlfe.Memoization.memoize', memoize_with_args).start()

# TODO: this is super messy, but I'm not sure how to do a better job. Otherwise memoized functions hold their value between runs
