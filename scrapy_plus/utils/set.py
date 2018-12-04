#coding:utf-8

from ..conf.default_settings import *
import redis

class BaseFilterSet(object):
    def _add_fp(self, fp):
        pass

    def _is_filter(self, fp):
        pass


class PythonFilterSet(BaseFilterSet):
    def __init__(self):
        self._fp_set = set()

    def _add_fp(self, fp):
        self._fp_set.add(fp)

    def _is_filter(self, fp):
        if fp in self._fp_set:
            return True
        else:
            return False


class RedisFilterSet(BaseFilterSet):
    def __init__(self):
        self._fp_set = redis.Redis(host=REDIS_REDIS_HOST, port=REDIS_REDIS_PORT, db=REDIS_REDIS_DB)

    def _add_fp(self, fp):
        self._fp_set.sadd(REDIS_REDIS_NAME, fp)

    def _is_filter(self, fp):
        return self._fp_set.sismember(REDIS_REDIS_NAME, fp)






