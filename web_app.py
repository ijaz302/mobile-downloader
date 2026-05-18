import os
import subprocess
from flask import Flask, render_template, request

app = Flask(__name__)

# Server start hote hi yt-dlp ko automatic update karne ka function
def update_ytdlp():
    try:
        print("Checking for yt-dlp updates...")
        # Live server par bina rukawat update karne ke liye switch
        subprocess.run(["pip", "install", "--upgrade", "yt-dlp"], check=True)
        print("yt-dlp is up to date!")
    except Exception as e:
        print(f"Update note: {e}")

# Run the update
update_ytdlp()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/download', methods=['POST'])
def download_video():
    video_url = request.form.get('video_url')
    if not video_url:
        return "Error: Please provide a valid YouTube link.", 400

    try:
        # YouTube security bypass configurations
        command = [
            'yt-dlp',
            '-g',  # Direct downloadable link nikalne ke liye
            '--no-playlist',
            '--add-header', 'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
            '-f', 'best',
            video_url
        ]

        result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, check=True)
        direct_download_url = result.stdout.strip()

        # Success Page (SaveFrom Design Template)
        return f"""
        <html>
        <head>
            <title>Download Ready</title>
            <script src="https://cdn.jsdelivr.net/npm/@tailwindcss/browser@4"></script>
        </head>
        <body class="bg-slate-900 text-white flex flex-col items-center justify-center min-h-screen p-4">
            <div class="text-center p-8 bg-slate-800 rounded-xl shadow-2xl border border-slate-700 max-w-md w-full">
                <span class="text-6xl">🎉</span>
                <h2 class="text-2xl font-bold mt-4 mb-2 text-green-400">Video Link Ready!</h2>
                <p class="text-gray-400 text-sm mb-6">Click the green button below to save your video directly.</p>
                
                <a href="{direct_download_url}" target="_blank" download class="bg-green-500 hover:bg-green-600 text-slate-900 font-bold px-6 py-4 rounded-xl text-lg block transition transform hover:scale-105 shadow-lg">
                    🟢 Download Video Now
                </a>
                
                <a href="/" class="text-sm text-gray-400 hover:text-white mt-6 block transition underline">
                    ← Download Another Video
                </a>
            </div>
        </body>
        </html>
        """

    except subprocess.CalledProcessError as e:
        error_msg = e.stderr if e.stderr else "Could not fetch stream links."
        return f"""
        <html>
        <head><script src="https://cdn.jsdelivr.net/npm/@tailwindcss/browser@4"></script></head>
        <body class="bg-slate-900 text-white flex flex-col items-center justify-center min-h-screen p-4">
            <div class="text-center p-8 bg-slate-800 rounded-xl border border-red-500 max-w-md w-full">
                <h2 class="text-2xl font-bold text-red-500 mb-2">⚠️ Download Failed</h2>
                <p class="text-gray-300 text-sm mb-4">YouTube temporary block triggered. Please try again after 5 seconds.</p>
                <p class="text-xs text-gray-500 bg-slate-950 p-2 rounded text-left overflow-x-auto">Log: {error_msg}</p>
                <a href="/" class="text-sm text-green-400 hover:underline mt-4 block">← Go Back</a>
            </div>
        </body>
        </html>
        """

if __name__ == '__main__':
    # Cloud platform hosting port deployment setup
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
