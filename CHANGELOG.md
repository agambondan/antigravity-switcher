# Changelog

All notable changes to **Antigravity Switcher (`agys`)** will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

---

## [1.0.0] - 2026-11-06

### Added
- **Multi-Account Keyring Vault:** Instant 1-second switching between Google One accounts without browser re-login or credential loss.
- **Live 9Router Quota Intelligence:** Real-time tracking of 5-hour session limits and weekly quotas for Claude 3.5 Sonnet, GPT, Gemini Pro, and Gemini 4 Argon.
- **Gemini 4 Argon Pool Support:** Full support for `gemini-4-argon-high`, `medium`, and `low` shared quotas.
- **Smart Quota-First Sorting:** Automatic ranking prioritizing accounts with active 5-hour quota, followed by weekly limits, and cooldown reset timers.
- **Auto-Best Switcher (`agys auto`):** Single command to automatically detect and activate the account with the highest quota.
- **Collision-Free Auto-Resume (`agyr`):** Detects running PTY sessions (`● pts/1`, `● pts/3`) to avoid terminal collisions and seamlessly resumes the active conversation.
- **Auto Permissions Bypass:** Automatic `--dangerously-skip-permissions` injection across commands and shell aliases.
- **Background Watcher Daemon (`agys daemon`):** Detached monitor with native Linux desktop alerts (`notify-send`) when exhausted accounts finish cooldown.
- **Sub-Millisecond Statusline (`agys statusline`):** High-performance cached statusline string (< 1ms) for Tmux statusbar and Zsh `RPROMPT`.
- **Interactive TUI & Desktop GUI:** Terminal menu with Rich formatting, keyboard hotkeys, and Zenity GTK modal dialogs.
- **Official Landing Page:** Deployed on Vercel with responsive Dark Mode, interactive visual tabs, and IndexNow/SEO optimization.
