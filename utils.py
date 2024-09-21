#
#
#   Utils
#
#

import itertools

from tqdm import tqdm


def brute_force(character_set: str, min_length: int | None = None, max_length: int | None = None,
                progress: bool = False):
    if min_length is None:
        min_length = 1

    if max_length is None:
        def password_length_iter():
            i = min_length
            while True:
                yield i
                i += 1
    else:
        def password_length_iter():
            return range(min_length, max_length + 1)

    for password_length in tqdm(password_length_iter(), disable=not progress):
        pbar = tqdm(total=len(character_set) ** password_length, leave=False, disable=not progress)

        for combination in itertools.product(character_set, repeat=password_length):
            password_to_try = "".join(combination)

            yield password_to_try

            pbar.update(1)
