# AGENTS
# Repository guidance for automated coding agents.
# Keep this file up to date as workflows evolve.

## Scope and intent

- This repo collects scripts and configuration snippets for OPNsense/FreeBSD
  network services and operational tooling.
- Primary languages: POSIX shell, Python 3, awk, and INI-like configs.
- Many scripts assume root or service users on an appliance. Be conservative
  with side effects and document any behavior changes.

## Source of truth

- Installation/operational notes live in `README.md`.
- Additional technical notes live in `technical_notes.md`.
- No Cursor rules (`.cursor/rules/`, `.cursorrules`) or Copilot instructions
  (`.github/copilot-instructions.md`) exist in this repo.

## Build, lint, and test commands

- There is no formal build system or test suite in the repo.
- No lint configuration files were found (no `pyproject.toml`, `setup.cfg`,
  `.flake8`, `shellcheck` config, etc.).
- Use ad-hoc execution commands and sanity checks when touching scripts.

### Common execution commands (FreeBSD/OPNsense)

- Run the pfctl scan helper:
  - `sudo /usr/local/bin/python3 /root/bin/scan_pfctl.py`
- Run the cron wrapper for scanning:
  - `sudo /usr/local/opnsense/scripts/custom/nmap_cron.sh`
- Run the USB NIC rename helper:
  - `sudo /usr/local/sbin/usb_nic_rename.sh ue0`
- Start the uploadthing service (rc.d style):
  - `sudo service uploadthing start`

### Single-test equivalents

- There is no test runner; treat single-test runs as executing the individual
  script or config change in isolation.
- Prefer dry runs or safe command variants where possible (see style rules).

## Code style guidelines

### General

- Keep scripts small, explicit, and operationally safe; avoid implicit defaults.
- Prefer clarity over cleverness; this repo is used in ops workflows.
- Use ASCII only unless the file already contains non-ASCII characters.
- Preserve existing file layout; many files map directly to system paths.

### File locations and ownership

- `bin/` contains scripts expected to be on the appliance PATH (e.g. `/root/bin`).
- `files/` mirrors `/usr/local/...` paths on OPNsense for deployment.
- `etc/` stores reference lists and operational notes.
- `Mikrotik/` contains router configuration artifacts.

### Shell script conventions

- Use `#!/bin/sh` for portable scripts unless a tool requires bash.
- Avoid bashisms; use POSIX constructs and test (`[ ]`) syntax.
- Use `set -euo pipefail` only when you have audited all call sites; most scripts
  are run under cron/rc where partial failure handling is expected.
- Quote variables and paths: `"$var"`, `"${path}"`.
- Use explicit paths for system binaries when side effects matter
  (e.g. `/sbin/ifconfig`, `/usr/sbin/daemon`).
- Log operational output via `logger` or to a log file when used by cron.

### Python conventions

- Target `/usr/local/bin/python3` on FreeBSD/OPNsense.
- Standard library only unless explicitly documented.
- Keep imports grouped: standard library only, alphabetized.
- Use small, single-purpose functions; avoid global side effects at import time.
- Handle subprocess errors with `check=True` and surface actionable logs.
- Keep network calls explicit; timeouts or retries should be documented.

### Awk conventions

- Use the existing `#!/usr/bin/env -S awk -f` shebang when scripts are standalone.
- Keep scripts minimal and stream-friendly; avoid external command calls.

### Config/INI conventions

- Preserve existing keys and ordering; many files are read by system daemons.
- Use lowercase keys where already established.
- Avoid trailing whitespace; keep single blank lines between sections.

### Imports and dependencies

- Do not introduce new third-party dependencies without documenting installation
  steps in `README.md`.
- If you must add a dependency, prefer system packages available on FreeBSD.
- For Python, stick to stdlib unless strictly needed.

### Formatting

- Use 4-space indentation in Python.
- Use 2-space indentation in shell when blocks are nested.
- Keep lines under ~100 characters when practical, but avoid forced wrapping in
  config files that are path-sensitive.

### Naming conventions

- Scripts: use descriptive, lowercase names with underscores when needed.
- Functions: `snake_case` in Python, lower_snake in shell functions.
- Config files: preserve upstream naming; do not rename without migration plan.

### Error handling and safety

- Fail fast on critical errors; log warnings for non-fatal issues.
- Prefer explicit `exit 1` for unrecoverable states in scripts.
- Validate inputs (e.g. interface names, subnet prefixes) before use.
- Be careful with network-impacting operations (pfctl, ifconfig, firewall rules).

### Logging and observability

- Cron/daemon scripts should log to a predictable file or syslog.
- Include timestamps for operational logs where feasible.
- Avoid noisy output on success; log only when something changes.

### Security considerations

- Do not commit secrets or real MAC/IPs; use placeholders where possible.
- Avoid embedding credentials; rely on system config or env vars.
- Validate external URLs before use; prefer HTTPS when possible.

## Technical notes incorporated

- `technical_notes.md` includes operational command snippets such as
  `VBoxManage createmedium` and `nmap` XML to JSON conversions.
- Treat those notes as examples; avoid running them automatically or as part of
  scripts without explicit user approval.

## Operational context (from README)

- Installation assumes cloning as root into `/root` and linking `examdns/bin`.
- OPNsense configuration touches Unbound, NAT redirects, DOH aliasing, and cron.
- There are explicit steps for USB NIC persistence and rc.d service setup.

## Working with this repo

- Keep config files in `files/` aligned with their target system paths.
- When adding new scripts, update `README.md` with deployment notes.
- If you add a new operational workflow, document it in `technical_notes.md`.

