import unittest
from unittest.mock import patch, MagicMock
from vdl.downloader import VideoDownloader, VideoDownloadError

class TestVideoDownloader(unittest.TestCase):
    def setUp(self):
        self.downloader = VideoDownloader()
        
    @patch('yt_dlp.YoutubeDL')
    def test_youtube_download(self, mock_ytdl):
        mock_instance = MagicMock()
        mock_ytdl.return_value.__enter__.return_value = mock_instance
        
        url = "https://www.youtube.com/watch?v=test"
        self.downloader.download(url)
        mock_instance.download.assert_called_once_with([url])
        
    @patch('yt_dlp.YoutubeDL')
    def test_bilibili_download(self, mock_ytdl):
        mock_instance = MagicMock()
        mock_ytdl.return_value.__enter__.return_value = mock_instance
        
        url = "https://www.bilibili.com/video/test"
        self.downloader.download(url)
        mock_instance.download.assert_called_once_with([url])
        
    def test_invalid_url(self):
        with self.assertRaises(ValueError):
            self.downloader.download("invalid_url")
            
    @patch('yt_dlp.YoutubeDL')
    def test_format_listing(self, mock_ytdl):
        mock_instance = MagicMock()
        mock_instance.extract_info.return_value = {
            'formats': [
                {'format_id': '1', 'ext': 'mp4', 'resolution': '1080p'},
                {'format_id': '2', 'ext': 'mp4', 'resolution': '720p'}
            ]
        }
        mock_ytdl.return_value.__enter__.return_value = mock_instance
        
        formats = self.downloader.list_formats("https://www.youtube.com/watch?v=test")
        self.assertEqual(len(formats), 2)
        mock_instance.extract_info.assert_called_once_with("https://www.youtube.com/watch?v=test", download=False)

if __name__ == '__main__':
    unittest.main()
