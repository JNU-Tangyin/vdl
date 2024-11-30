import unittest
from unittest.mock import patch, MagicMock
from click.testing import CliRunner
from vdl.cli import cli
from vdl.downloader import VideoDownloader, VideoDownloadError

class TestCLI(unittest.TestCase):
    def setUp(self):
        self.runner = CliRunner()
        
    def test_cli_help(self):
        result = self.runner.invoke(cli, ['--help'])
        self.assertEqual(result.exit_code, 0)
        self.assertIn('VDL - Video Downloader CLI', result.output)
        
    @patch('vdl.cli.VideoDownloader')
    def test_download_command(self, mock_downloader_class):
        mock_downloader = MagicMock()
        mock_downloader_class.return_value = mock_downloader
        
        result = self.runner.invoke(cli, ['download', 'https://www.youtube.com/watch?v=test'])
        self.assertEqual(result.exit_code, 0)
        mock_downloader.download.assert_called_once_with(
            'https://www.youtube.com/watch?v=test',
            quality='best',
            output=None
        )
        
    @patch('vdl.cli.VideoDownloader')
    def test_download_with_options(self, mock_downloader_class):
        mock_downloader = MagicMock()
        mock_downloader_class.return_value = mock_downloader
        
        result = self.runner.invoke(cli, [
            'download',
            'https://www.youtube.com/watch?v=test',
            '--quality', '720p',
            '--output', 'video.mp4',
            '--subtitle'
        ])
        self.assertEqual(result.exit_code, 0)
        mock_downloader.download.assert_called_once_with(
            'https://www.youtube.com/watch?v=test',
            quality='720p',
            output='video.mp4'
        )
        
    @patch('vdl.cli.VideoDownloader')
    def test_download_error(self, mock_downloader_class):
        mock_downloader = MagicMock()
        mock_downloader.download.side_effect = VideoDownloadError('Download failed')
        mock_downloader_class.return_value = mock_downloader
        
        result = self.runner.invoke(cli, ['download', 'https://www.youtube.com/watch?v=test'])
        self.assertEqual(result.exit_code, 0)
        self.assertIn('Download Error: Download failed', result.output)
        
    @patch('vdl.cli.VideoDownloader')
    def test_formats_command(self, mock_downloader_class):
        mock_downloader = MagicMock()
        mock_downloader.list_formats.return_value = [
            '137 - 1080p (mp4)',
            '136 - 720p (mp4)'
        ]
        mock_downloader_class.return_value = mock_downloader
        
        result = self.runner.invoke(cli, ['formats', 'https://www.youtube.com/watch?v=test'])
        self.assertEqual(result.exit_code, 0)
        mock_downloader.list_formats.assert_called_once_with('https://www.youtube.com/watch?v=test')
        self.assertIn('Available formats:', result.output)
        
    @patch('vdl.cli.VideoDownloader')
    def test_formats_error(self, mock_downloader_class):
        mock_downloader = MagicMock()
        mock_downloader.list_formats.side_effect = VideoDownloadError('Format listing failed')
        mock_downloader_class.return_value = mock_downloader
        
        result = self.runner.invoke(cli, ['formats', 'https://www.youtube.com/watch?v=test'])
        self.assertEqual(result.exit_code, 0)
        self.assertIn('Format List Error: Format listing failed', result.output)
        
    def test_supported_command(self):
        result = self.runner.invoke(cli, ['supported'])
        self.assertEqual(result.exit_code, 0)
        self.assertIn('Supported Platforms:', result.output)
        self.assertIn('YouTube', result.output)
        self.assertIn('Bilibili', result.output)

if __name__ == '__main__':
    unittest.main()
