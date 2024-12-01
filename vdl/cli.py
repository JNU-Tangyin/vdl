import click
from rich.console import Console
from rich.table import Table
from vdl.downloader import VideoDownloader, VideoDownloadError
from urllib.parse import urlparse

console = Console()

def is_url(string):
    """Check if a string is a URL"""
    try:
        result = urlparse(string)
        return all([result.scheme, result.netloc])
    except:
        return False

def download_video(url, quality, output, subtitle, playlist):
    """Download video from URL"""
    try:
        downloader = VideoDownloader()
        if playlist and "list=" not in url:
            console.print("[yellow]Warning: Playlist flag set but URL doesn't appear to be a playlist[/yellow]")
        
        downloader.download(url, quality=quality, output=output)
        console.print("[green]Download completed successfully![/green]")
    except VideoDownloadError as e:
        console.print(f"[red]Download Error: {str(e)}[/red]")
    except Exception as e:
        console.print(f"[red]Unexpected Error: {str(e)}[/red]")

@click.group()
def cli():
    """VDL - Video Downloader CLI"""
    pass

@cli.command(name='')
@click.option('--quality', default='best', help='Video quality (e.g., 1080p, 720p)')
@click.option('--output', '-o', help='Output filename template')
@click.option('--subtitle/--no-subtitle', default=False, help='Download subtitles if available')
@click.option('--playlist/--no-playlist', default=False, help='Download as playlist')
@click.argument('url', required=True)
def download(url, quality, output, subtitle, playlist):
    """Download video from URL"""
    if not is_url(url):
        click.echo(f"Error: '{url}' is not a valid URL")
        return
    download_video(url, quality, output, subtitle, playlist)

@cli.command()
@click.argument('url')
def formats(url):
    """List available formats for URL"""
    try:
        downloader = VideoDownloader()
        formats = downloader.list_formats(url)
        
        table = Table(show_header=True, header_style="bold magenta")
        table.add_column("Format ID")
        table.add_column("Quality")
        table.add_column("Extension")
        
        for fmt in formats:
            parts = fmt.split(' - ', 1)
            if len(parts) == 2:
                format_id = parts[0]
                rest = parts[1].strip('()').split(' ', 1)
                quality = rest[0] if len(rest) > 1 else 'N/A'
                ext = rest[-1]
                table.add_row(format_id, quality, ext)
        
        console.print("\n[green]Available formats:[/green]")
        console.print(table)
    except VideoDownloadError as e:
        console.print(f"[red]Format List Error: {str(e)}[/red]")
    except Exception as e:
        console.print(f"[red]Unexpected Error: {str(e)}[/red]")

@cli.command()
def supported():
    """List supported platforms"""
    downloader = VideoDownloader()
    table = Table(show_header=True, header_style="bold magenta")
    table.add_column("Platform")
    table.add_column("Domain")
    
    for domain, platform in downloader.SUPPORTED_PLATFORMS.items():
        table.add_row(platform, domain)
    
    console.print("\n[green]Supported Platforms:[/green]")
    console.print(table)

if __name__ == '__main__':
    cli()
