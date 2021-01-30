"""Tests for our `pyMV2H compare_files` subcommand."""


from subprocess import PIPE, check_output
from unittest import TestCase
import os


class TestCompareFiles(TestCase):

    @classmethod
    def setUpClass(cls):

        current_path = os.path.dirname(__file__)
        current_path = os.path.join(current_path, '../../')

        cls._output_file = f'{current_path}/tests/input_files/output_java/output_test_cases.txt'
        cls._transcription_dir = f'{current_path}/tests/input_files/transcription_files'
        cls._replace_key = '${TRANSCRIPTION_DIR}'

    def test_if_file_exists(self):
        self.assertTrue(os.path.isfile(self._output_file), 'Can\'t find the output_file')

    def test_mv2h_output_from_python_and_java_should_be_equal(self):

        with open(self._output_file, 'r') as out_test_cases:
            command_line = None
            metrics = {}

            for line in out_test_cases:
                line = line.replace('\n', '')
                # Break line is a new case
                if not line:
                    # execute if got the command_line and metrics
                    if command_line and len(metrics.keys()) > 0:
                        self.check_output(command_line, metrics)

                    command_line = None
                    metrics = {}
                # next line is a command
                elif not command_line:
                    command_line = line
                #other lines are the metrics
                else:
                    name, value = line.replace(' ', '').split(':')
                    metrics[name] = value

    def check_output(self, command_line, metrics):
        command_line = command_line.replace(self._replace_key, self._transcription_dir)
        command_line = f'pyMV2H compare_files {command_line}'

        print('*' * 30)
        print(f'Running: {command_line}')
        output = check_output(
            command_line.split(' '),
            stderr=PIPE,
            timeout=20
        )
        lines = output.split('\n'.encode())
        python_version_metrics = self.parse_pymv2h_output(lines)
        for metric_name in metrics.keys():
            print(f'Java: {metrics}')
            print(f'Python: {python_version_metrics}')
            print('*' * 30)
            self.assertEqual(metrics[metric_name], python_version_metrics[metric_name])

    def parse_pymv2h_output(self, lines):
        metrics = {}
        for line in lines:
            output = line.decode('utf-8').replace(' ', '').replace('\n', '')
            if not output:
                continue
            name, value = output.split(':')
            metrics[name] = value
        return metrics
