from __future__ import absolute_import
from __future__ import unicode_literals

import os
import shelve
import shutil
import tempfile

from testify import assert_equal
from testify import run
from testify import setup
from testify import teardown
from testify import TestCase

from tron.serialize.runstate.shelvestore import ShelveKey
from tron.serialize.runstate.shelvestore import ShelveStateStore


class ShelveStateStoreTestCase(TestCase):

    @setup
    def setup_store(self):
        self.tmpdir = tempfile.mkdtemp()
        self.filename = os.path.join(self.tmpdir, 'state')
        self.store = ShelveStateStore(self.filename)

    @teardown
    def teardown_store(self):
        shutil.rmtree(self.tmpdir)

    def test__init__(self):
        assert_equal(self.filename, self.store.filename)

    def test_save(self):
        key_value_pairs = [
            (ShelveKey("one", "two"), {'this': 'data'}),
            (ShelveKey("three", "four"), {'this': 'data2'}),
        ]
        self.store.save(key_value_pairs)
        self.store.cleanup()

        stored_data = shelve.open(self.filename)
        for key, value in key_value_pairs:
            assert_equal(stored_data[str(key.key)], value)
        stored_data.close()

    def test_restore(self):
        self.store.cleanup()
        keys = [ShelveKey("thing", i) for i in range(5)]
        value = {'this': 'data'}
        store = shelve.open(self.filename)
        for key in keys:
            store[str(key.key)] = value
        store.close()

        self.store.shelve = shelve.open(self.filename)
        retrieved_data = self.store.restore(keys)
        for key in keys:
            assert_equal(retrieved_data[key], value)


if __name__ == "__main__":
    run()
