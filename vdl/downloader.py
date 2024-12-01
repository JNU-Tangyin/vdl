import yt_dlp
import os
import browser_cookie3
from typing import List, Dict, Optional
from urllib.parse import urlparse
from rich.progress import Progress

class VideoDownloadError(Exception):
    """Custom exception for video download errors"""
    pass

class VideoDownloader:
    SUPPORTED_PLATFORMS = {
        'youtube.com': 'YouTube',
        'youtu.be': 'YouTube',
        'bilibili.com': 'Bilibili'
    }
    
    def __init__(self):
        self.cookies = self._get_cookies()
    
    def _get_cookies(self) -> Dict:
        """Get cookies from Chrome browser"""
        try:
            return browser_cookie3.chrome()
        except Exception:
            return None
    
    def _get_platform(self, url: str) -> str:
        """Determine the platform from URL"""
        try:
            domain = urlparse(url).netloc.lower()
            base_domain = '.'.join(domain.split('.')[-2:])
            
            if base_domain not in self.SUPPORTED_PLATFORMS:
                raise ValueError(f"Unsupported platform. Supported platforms: {', '.join(self.SUPPORTED_PLATFORMS.keys())}")
            
            return self.SUPPORTED_PLATFORMS[base_domain]
        except Exception as e:
            if not domain:  # Invalid URL format
                raise ValueError(f"Invalid URL format: {url}")
            raise e
    
    def _get_ydl_opts(self, quality: str = 'best', output: Optional[str] = None) -> Dict:
        """Configure yt-dlp options"""
        format_spec = 'best'
        if quality != 'best':
            if quality.endswith('p'):
                format_spec = f'bestvideo[height<={quality[:-1]}]+bestaudio/best[height<={quality[:-1]}]'
            else:
                format_spec = quality
                
        opts = {
            'format': format_spec,
            'cookiesfrombrowser': ('chrome',),  # Always try to use Chrome cookies
            'progress_hooks': [self._progress_hook],
            'quiet': True,  # Suppress yt-dlp's output
            'no_warnings': True  # Suppress warnings
        }
        
        if output:
            opts['outtmpl'] = output
            
        return opts
    
    def _progress_hook(self, d: Dict):
        """Handle download progress"""
        if d['status'] == 'downloading' and hasattr(self, '_progress'):
            total = d.get('total_bytes') or d.get('total_bytes_estimate', 0)
            downloaded = d.get('downloaded_bytes', 0)
            
            self._progress.update(
                self._task_id,
                completed=downloaded,
                total=total if total > 0 else None,
                description=f"Downloading: {d.get('filename', '')}"
            )
    
    def download(self, url: str, quality: str = 'best', output: Optional[str] = None):
        """Download video from URL"""
        try:
            opts = self._get_ydl_opts(quality, output)
            
            with Progress() as progress:
                self._progress = progress
                self._task_id = progress.add_task("Starting download...", total=None)
                
                with yt_dlp.YoutubeDL(opts) as ydl:
                    ydl.download([url])
                    
        except ValueError as e:
            raise e
        except Exception as e:
            raise VideoDownloadError(f"Failed to download video: {str(e)}")
    
    def list_formats(self, url: str) -> List[str]:
        """List available formats for URL"""
        try:
            self._get_platform(url)  # Validate URL
            opts = {
                'cookiesfrombrowser': ('chrome',) if self.cookies else None,
                'quiet': True,
                'no_warnings': True
            }
            
            with yt_dlp.YoutubeDL(opts) as ydl:
                info = ydl.extract_info(url, download=False)
                formats = []
                for f in info.get('formats', []):
                    format_str = f"{f.get('format_id', 'N/A')} - "
                    if f.get('resolution') != 'audio only':
                        format_str += f"{f.get('resolution', 'N/A')} "
                    format_str += f"({f.get('ext', 'N/A')})"
                    formats.append(format_str)
                return formats
                
        except ValueError as e:
            raise e
        except Exception as e:
            raise VideoDownloadError(f"Failed to list formats: {str(e)}")
