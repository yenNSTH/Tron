from __future__ import absolute_import
from __future__ import unicode_literals

import tempfile

import action_runner
import mock
from testify import assert_equal
from testify import setup
from testify import setup_teardown
from testify import TestCase


class StatusFileTestCase(TestCase):

    @setup
    def setup_status_file(self):
        self.filename = tempfile.NamedTemporaryFile().name
        self.status_file = action_runner.StatusFile(self.filename)

    def test_get_content(self):
        command, proc, run_id = 'do this', mock.Mock(), 'Job.test.1'
        content = self.status_file.get_content(
            command=command, proc=proc, run_id=run_id,
        )
        expected = dict(
            run_id=run_id,
            command=command, pid=proc.pid,
            return_code=proc.returncode,
        )
        assert_equal(content, expected)


class RegisterTestCase(TestCase):
    mock_isdir = mock_status_file = None
    mock_makedirs = None

    @setup_teardown
    def patch_sys(self):
        with mock.patch('action_runner.os.path.isdir', autospec=True) as self.mock_isdir, \
                mock.patch('action_runner.os.makedirs', autospec=True) as self.mock_makedirs, \
                mock.patch('action_runner.os.access', autospec=True) as self.mock_access, \
                mock.patch('action_runner.StatusFile', autospec=True) as self.mock_status_file:
            self.output_path = '/bogus/path/does/not/exist'
            self.command = 'command'
            self.run_id = 'Job.test.1'
            self.proc = mock.Mock()
            yield

    def test_get_status_file_dir_does_not_exist(self):
        self.mock_isdir.return_value = False
        self.mock_access.return_value = True
        action_runner.get_status_file(self.output_path)
        self.mock_makedirs.assert_called_with(self.output_path)

    def test_get_status_file_dir_does_not_exist_create_fails(self):
        self.mock_isdir.return_value = False
        self.mock_access.return_value = True
        self.mock_makedirs.side_effect = OSError
        self.failUnlessRaises(
            OSError, action_runner.get_status_file, self.output_path,
        )

    def test_get_status_file_exists_not_writable(self):
        self.mock_isdir.return_value = True
        self.mock_access.return_value = False
        self.failUnlessRaises(
            OSError, action_runner.get_status_file, self.output_path,
        )

    @mock.patch('action_runner.sys.exit', autospec=True)
    def test_run_proc(self, mock_sys_exit):
        self.mock_isdir.return_value = True
        self.mock_access.return_value = True
        action_runner.run_proc(
            self.output_path, self.command, self.run_id, self.proc,
        )
        self.mock_status_file.assert_called_with(
            self.output_path + '/' + action_runner.STATUS_FILE,
        )
        self.mock_status_file.return_value.wrap.assert_called_with(
            command=self.command,
            run_id=self.run_id,
            proc=self.proc,
        )
        self.proc.wait.assert_called_with()
        mock_sys_exit.assert_called_with(self.proc.returncode)
