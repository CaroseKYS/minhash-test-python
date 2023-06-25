from datasketch import LeanMinHash
from lib.minhash_original import MinHash as OriginalMinhash
from lib.minhash_optimized import MinHash as OptimizedMinhash
from lib.minhash_cached import MinHash as CachedMinhash
import re

_split = re.compile(r'\s+')
_coding = 'utf8'


def _encode_text(text1: str, text2: str):
    return (
        [(item.strip()).encode(_coding) for item in _split.split(text1)],
        [(item.strip()).encode(_coding) for item in _split.split(text2)]
    )


def jaccard_original(text1: str, text2: str, num_perm: int = 128, seed: int = 1) -> float:
    data1, data2 = _encode_text(text1, text2)

    m1, m2 = OriginalMinhash(num_perm=num_perm, seed=seed), OriginalMinhash(num_perm=num_perm, seed=seed)

    m1.update_batch(data1)
    m2.update_batch(data2)

    return m1.jaccard(m2)


def jaccard_optimized(text1: str, text2: str, num_perm: int = 128, seed: int = 1) -> float:
    data1, data2 = _encode_text(text1, text2)

    m1, m2 = OptimizedMinhash(num_perm=num_perm, seed=seed), OptimizedMinhash(num_perm=num_perm, seed=seed)

    m1.update_batch(data1)
    m2.update_batch(data2)

    return m1.jaccard(m2)


def jaccard_cached(text1: str, text2: str, num_perm: int = 128, seed: int = 1) -> float:
    data1, data2 = _encode_text(text1, text2)

    m1, m2 = CachedMinhash(num_perm=num_perm, seed=seed), CachedMinhash(num_perm=num_perm, seed=seed)

    m1.update_batch(data1)
    m2.update_batch(data2)

    return m1.jaccard(m2)


def jaccard_on_lean_minhash_optimized(text1: str, text2: str, num_perm: int = 128, seed: int = 1) -> float:
    data1, data2 = _encode_text(text1, text2)

    m1, m2 = OptimizedMinhash(num_perm=num_perm, seed=seed), OptimizedMinhash(num_perm=num_perm, seed=seed)

    m1.update_batch(data1)
    m2.update_batch(data2)

    lm1, lm2 = LeanMinHash(minhash=m1), LeanMinHash(minhash=m2)

    return lm1.jaccard(lm2)


def jaccard_on_lean_minhash_original(text1: str, text2: str, num_perm: int = 128, seed: int = 1) -> float:
    data1, data2 = _encode_text(text1, text2)

    m1, m2 = OriginalMinhash(num_perm=num_perm, seed=seed), OriginalMinhash(num_perm=num_perm, seed=seed)

    m1.update_batch(data1)
    m2.update_batch(data2)

    lm1, lm2 = LeanMinHash(minhash=m1), LeanMinHash(minhash=m2)

    return lm1.jaccard(lm2)


def jaccard_on_lean_minhash_cached(text1: str, text2: str, num_perm: int = 128, seed: int = 1) -> float:
    data1, data2 = _encode_text(text1, text2)

    m1, m2 = CachedMinhash(num_perm=num_perm, seed=seed), CachedMinhash(num_perm=num_perm, seed=seed)

    m1.update_batch(data1)
    m2.update_batch(data2)

    lm1, lm2 = LeanMinHash(minhash=m1), LeanMinHash(minhash=m2)

    return lm1.jaccard(lm2)
