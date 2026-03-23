# homekitlink_ffmpeg/__init__.py
import os
import platform


def _get_binary(name: str) -> str:
    """Get the path to the appropriate binary for the current architecture."""
    package_dir = os.path.abspath(os.path.dirname(__file__))

    arch = platform.machine()
    if arch == 'x86_64':
        binary_path = os.path.join(package_dir, 'ffmpeg_binaries', 'x86', name)
    elif arch == 'arm64':
        binary_path = os.path.join(package_dir, 'ffmpeg_binaries', 'arm', name)
    else:
        raise ValueError(f"Unsupported architecture: {arch}")

    if not os.path.isfile(binary_path):
        raise FileNotFoundError(f"Binary '{name}' not found for the architecture at {binary_path}")

    return binary_path


def get_ffmpeg_binary():
    """Get the path to the appropriate FFmpeg binary."""
    return _get_binary('ffmpeg')


def get_ffprobe_binary():
    """Get the path to the appropriate FFprobe binary."""
    return _get_binary('ffprobe')