import os
import sys
import time
import subprocess
import importlib.machinery
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich import box

# Load the agys module
loader = importlib.machinery.SourceFileLoader('agys', '/home/firman/works/me/antigravity-switcher/bin/agys')
mod = loader.load_module()

assets_dir = '/home/firman/works/me/antigravity-switcher/assets'
frames_dir = f'{assets_dir}/frames'
os.makedirs(frames_dir, exist_ok=True)

WIDTH = 135

print("1. Generating Frame 1 (agys list)...")
c1 = Console(record=True, width=WIDTH)
mod.console = c1
c1.print("[bold green]firman@box:~/works$[/bold green] [bold white]agys list[/bold white]\n")
mod.list_accounts_table(force_refresh=False)
with open(f'{frames_dir}/f1.svg', 'w') as f:
    f.write(c1.export_svg(title='1. agys list - Live Accounts & Quota Tracker'))

print("2. Generating Frame 2 (agys usage)...")
c2 = Console(record=True, width=WIDTH)
mod.console = c2
c2.print("[bold green]firman@box:~/works$[/bold green] [bold white]agys usage[/bold white]\n")
mod.show_quota_tracker(force_refresh=False)
with open(f'{frames_dir}/f2.svg', 'w') as f:
    f.write(c2.export_svg(title='2. agys usage - Detailed Progress Tracker'))

print("3. Generating Frame 3 (agys auto)...")
c3 = Console(record=True, width=WIDTH)
mod.console = c3
c3.print("[bold green]firman@box:~/works$[/bold green] [bold white]agys auto[/bold white]\n")
c3.print(Panel("[bold green]✔ Switched active account to: agamgans234@gmail.com (Plus)[/bold green]\n[dim]Antigravity CLI (agy) is ready to use with this account.[/dim]", border_style="green"))
c3.print(Panel("[bold green]✔ Auto-selected akun dengan kuota terbanyak:[/bold green]\n[bold white]agamgans234@gmail.com[/bold white] (Plan: [bold cyan]Plus[/bold cyan] | Claude 5h: [bold yellow]--[/bold yellow] | Claude Wk: [bold green]100%[/bold green])", border_style="bright_blue"))
c3.print("\n[dim]Tip: Jalankan 'agyr' untuk langsung auto-switch dan resume task terbaru![/dim]")
with open(f'{frames_dir}/f3.svg', 'w') as f:
    f.write(c3.export_svg(title='3. agys auto - Auto-select Account with Highest Quota'))

print("4. Generating Frame 4 (agyr - Smart Auto-resume)...")
c4 = Console(record=True, width=WIDTH)
mod.console = c4
c4.print("[bold green]firman@box:~/works$[/bold green] [bold white]agyr[/bold white]\n")
c4.print(Panel("[bold green]✔ Akun aktif saat ini (agamgans234@gmail.com) sudah memiliki kuota terbanyak![/bold green]\nPlan: [bold cyan]Plus[/bold cyan] | Claude 5h: [bold yellow]--[/bold yellow] | Claude Wk: [bold green]100%[/bold green]", border_style="green"))

convs = mod.get_recent_conversations()
table = Table(
    title="Daftar Percakapan Antigravity (/home/firman/works/me/saas-jangkauin)",
    box=box.ROUNDED,
    header_style="bold cyan",
    show_lines=True
)
table.add_column("#", justify="center", style="bold yellow", width=4)
table.add_column("Status", justify="center", width=16)
table.add_column("Judul Percakapan (Task)", style="bold white", width=44)
table.add_column("Terakhir Aktif", justify="center", style="dim", width=14)
table.add_column("Steps", justify="right", style="cyan", width=8)
table.add_column("Workspace", style="dim", width=16)

default_idx = 1
for i, c in enumerate(convs, 1):
    if not c["active_on"]:
        default_idx = i
        break

for idx, c in enumerate(convs[:6], 1):
    status_str = f"[bold yellow]● {c['active_on']}[/bold yellow]" if c['active_on'] else "[bold green]○ SIAP[/bold green]"
    ws_label = "Current Repo" if c["is_current_ws"] else "Other"
    title_disp = f"{c['title']} [green](terbaru)[/green]" if idx == default_idx else c['title']
    table.add_row(str(idx), status_str, title_disp, c['relative_time'], str(c['step_count']), ws_label)

c4.print(table)
c4.print(f"\nPilih nomor percakapan untuk di-resume [{default_idx}]: [bold green]{default_idx}[/bold green]")
cid = convs[default_idx-1]['conversation_id']
c4.print(f"\n[bold green]Meluncurkan 'agy --dangerously-skip-permissions --conversation {cid}'...[/bold green]")
with open(f'{frames_dir}/f4.svg', 'w') as f:
    f.write(c4.export_svg(title='4. agyr - Smart Resume & Permission Bypass'))

print("Rendering SVGs to PNG via headless Chrome...")
for i in range(1, 5):
    svg_file = f"{frames_dir}/f{i}.svg"
    png_file = f"{frames_dir}/f{i}.png"
    cmd = [
        "google-chrome",
        "--headless",
        "--disable-gpu",
        f"--screenshot={png_file}",
        "--window-size=1280,720",
        f"file://{svg_file}"
    ]
    subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True)
    print(f"  Rendered {png_file}")

# Also update the primary screenshots
subprocess.run(["cp", f"{frames_dir}/f1.png", f"{assets_dir}/screenshot-list.png"], check=True)
subprocess.run(["cp", f"{frames_dir}/f2.png", f"{assets_dir}/screenshot-quota.png"], check=True)
subprocess.run(["cp", f"{frames_dir}/f4.png", f"{assets_dir}/screenshot-resume.png"], check=True)

print("Encoding GIF via ffmpeg...")
gif_path = f"{assets_dir}/demo.gif"
# 2.5 seconds per frame = 0.4 fps input, filter palettegen for high crisp quality
cmd_gif = [
    "ffmpeg", "-y",
    "-framerate", "1/2.5",
    "-i", f"{frames_dir}/f%d.png",
    "-filter_complex", "[0:v]scale=1280:720:force_original_aspect_ratio=decrease,split[a][b];[a]palettegen=stats_mode=full[p];[b][p]paletteuse=dither=bayer:bayer_scale=3",
    gif_path
]
subprocess.run(cmd_gif, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True)
print(f"  Created {gif_path} ({os.path.getsize(gif_path)} bytes)")

print("Encoding MP4 via ffmpeg...")
mp4_path = f"{assets_dir}/demo.mp4"
# MP4 video with smooth presentation (30fps output, loop frames)
cmd_mp4 = [
    "ffmpeg", "-y",
    "-framerate", "1/2.5",
    "-i", f"{frames_dir}/f%d.png",
    "-c:v", "libx264",
    "-r", "30",
    "-pix_fmt", "yuv420p",
    "-vf", "scale=1280:720",
    mp4_path
]
subprocess.run(cmd_mp4, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True)
print(f"  Created {mp4_path} ({os.path.getsize(mp4_path)} bytes)")

print("All assets successfully generated!")
