# CHANGELOG

[Back](./README.md)
[CHANGELOG for user](./CHANGELOG.md)

## [0.2.0] (BETA) – 2026/04/09
*major architecture cleanup and new shapes.*

### Added
- **Triangle Module:** Finally added the `triangle` submodule. It’s fully loaded with `engine.py` for the math and `usecase.py` for the logic flow.
- **Version Sync Engine:** Created `system/debug/sync.py`. This tool makes sure the main MATEC version and all internal Python file versions stay in sync automatically—no more manual updates.
- **Centralized Helper:** Added `system/debug/helper.py`. I moved all the input length validation logic here to keep things tidy.

### Changed
- **Config Overhaul:** Moved path-handling from `system/config.yml` straight into `system/settings/manager.py`. The config file is much cleaner now since it doesn't have to worry about folder locations.
- **Engine Refactor:** Polished all `engine.py` files in the submodules to make the execution more consistent and optimized.
- **Loader Update:** `system/loader.py` doesn't touch paths anymore; its only job now is pure loading. Everything else is handled by the Settings Manager.
- **Doc Link Fix:** Patched the documentation link in `main.py` to point to the GitHub blob instead of a local path.

### Fixed
- **Redundancy Cleanup:** Stripped out duplicate path-handling code across `config.yml`, `loader.py`, and `manager.py`. No more useless copy-pasted logic.
- **Validation Flow:** Successfully migrated validation logic from `usecase.py` to the new `helper.py`. Sticking to the DRY (*Don't Repeat Yourself*) principle.

---

<details>
<summary><b>v0.1.1 beta 2026/04/05</b></summary>

*fixing annoying bugs*

### Changed
- **Simpler API:** Cleaned up the `scan()` function by removing the `recursive` parameter that wasn't being used anyway.
- **UI Padding:** Fixed the terminal output alignment so the version columns actually line up nicely.
- **Standard Return:** Made sure the `parse()` function always returns a `dict` (even if the input is empty) to stop the app from crashing.

### Fixed
- **Path Bug:** Fixed a wrong index issue when joining the root folder that was making the scanner fail.
- **Parser Logic:** Fixed a bug where the second argument was being ignored when a user typed a command.
- **Crash Fix:** Got rid of those `NoneType` errors caused by empty inputs.

</details>

---

<details>
<summary><b>v0.1.0 beta 2026/04/03</b></summary>

*initial release.*

### Added
- **Core App:** Initial architecture of MATEC (Math Tech).
- **Initial Shapes:** Basic modules for `Circle`, `Square`, and `Rectangle`.
- **Base System:** First versions of the Loader, Settings Manager, and Parser.

</details>

```text
you might wondering why my english is good? absolutely! it's AI and yk, idk is this really accurate, you can just check it by yourself i guess
```