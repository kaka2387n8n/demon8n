#!/usr/bin/env python3
"""
Video Editor - FFmpeg wrapper for video processing
"""

import subprocess
import sys
from pathlib import Path

class VideoEditor:
    def __init__(self, input_file, output_file):
        self.input_file = input_file
        self.output_file = output_file
    
    def add_voiceover(self, audio_file):
        """Add voiceover to video"""
        cmd = [
            'ffmpeg',
            '-i', self.input_file,
            '-i', audio_file,
            '-c:v', 'copy',
            '-c:a', 'aac',
            '-shortest',
            self.output_file
        ]
        subprocess.run(cmd, check=True)
        print(f"✅ Voiceover added: {self.output_file}")
    
    def add_subtitles(self, subtitle_file):
        """Add subtitles to video"""
        cmd = [
            'ffmpeg',
            '-i', self.input_file,
            '-i', subtitle_file,
            '-c:v', 'copy',
            '-c:a', 'copy',
            '-c:s', 'mov_text',
            self.output_file
        ]
        subprocess.run(cmd, check=True)
        print(f"✅ Subtitles added: {self.output_file}")
    
    def resize(self, width, height):
        """Resize video"""
        cmd = [
            'ffmpeg',
            '-i', self.input_file,
            '-vf', f'scale={width}:{height}',
            '-c:a', 'copy',
            self.output_file
        ]
        subprocess.run(cmd, check=True)
        print(f"✅ Video resized to {width}x{height}: {self.output_file}")
    
    def add_thumbnail(self, thumbnail_file, time='00:00:05'):
        """Extract frame as thumbnail"""
        cmd = [
            'ffmpeg',
            '-i', self.input_file,
            '-ss', time,
            '-vframes', '1',
            thumbnail_file
        ]
        subprocess.run(cmd, check=True)
        print(f"✅ Thumbnail created: {thumbnail_file}")

if __name__ == "__main__":
    print("🎬 Video Editor - FFmpeg Wrapper")
    print("Use this to edit videos for YouTube automation")
