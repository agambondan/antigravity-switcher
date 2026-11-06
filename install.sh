#!/usr/bin/env bash
# Antigravity Switcher (agys) Installer
set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
BIN_SRC="$SCRIPT_DIR/bin/agys"
TARGET_DIR="$HOME/.local/bin"

echo "=========================================="
echo "  Installing Antigravity Switcher (agys)  "
echo "=========================================="

mkdir -p "$TARGET_DIR"

# 1. Install / Symlink binary
echo "==> Creating executable symlinks in $TARGET_DIR..."
chmod +x "$BIN_SRC"
ln -sf "$BIN_SRC" "$TARGET_DIR/agys"
ln -sf "$BIN_SRC" "$TARGET_DIR/agy-switch"
ln -sf "$BIN_SRC" "$TARGET_DIR/antigravity-switch"

# 2. Check Python dependencies
echo "==> Checking required Python dependencies..."
python3 -c "import keyring" 2>/dev/null || {
    echo "    Installing 'keyring' via pip..."
    python3 -m pip install --quiet --upgrade keyring
}
python3 -c "import rich" 2>/dev/null || {
    echo "    Installing 'rich' via pip..."
    python3 -m pip install --quiet --upgrade rich
}

# 3. Add shell aliases if not present
setup_shell_aliases() {
    local rc_file="$1"
    if [ -f "$rc_file" ]; then
        if ! grep -q 'alias agy=' "$rc_file"; then
            echo 'alias agy="agy --dangerously-skip-permissions"' >> "$rc_file"
            echo "    Added 'agy' bypass alias to $rc_file"
        fi
        if ! grep -q 'alias agyr=' "$rc_file"; then
            echo 'alias agyr="agys auto -c"' >> "$rc_file"
            echo "    Added 'agyr' auto-resume alias to $rc_file"
        fi
    fi
}

echo "==> Setting up shell aliases..."
setup_shell_aliases "$HOME/.zshrc"
setup_shell_aliases "$HOME/.bashrc"

echo ""
echo "✔ Antigravity Switcher successfully installed!"
echo ""
echo "Available commands:"
echo "  agys               - Launch interactive TUI menu"
echo "  agys auto          - Automatically switch to account with highest quota"
echo "  agyr (or agys auto -c) - Auto-switch & resume active conversation immediately"
echo "  agys list          - List all accounts with live quotas & plan badges"
echo "  agys usage         - Detailed quota dashboard with progress bars"
echo "  agys resume        - Interactive conversation picker"
echo ""
