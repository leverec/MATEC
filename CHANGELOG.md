# CHANGELOG

[Back](./README.md)
[CHANGELOG for dev](./changelog.dev.md)

## [0.3.1] (BETA) – 2026/04/18

*fixing some bugs :D*

### Fixed
- **Smarter Math Input:** I’ve improved how the app reads your formulas. You can now use x as a multiplication sign even when it's right next to constants like π (e.g., pix7x7 now works perfectly).
- **Automatic Multiplication:** Writing math feels more natural now. You can place numbers and symbols side-by-side (like π4 or 4pi), and the system will automatically know you mean to multiply them. No extra symbols required!

---

<details>
<summary><b>v0.3.0 beta 2026/04/15</b></summary>

*major refactor, O(1) optimization, and arithmetic expansion.*

### Added
- **Arithmetic Engine:** Integrated `eval()` as a backend for `submodulesB`. Added custom pre-processing for math symbols (π, √, ^, etc.) and support for implicit multiplication (e.g., `pix7^2`).
- **Debug Mode Implementation:** Introduced `sys.argv` detection. `debugMode` toggles between returning `None` (Normal) and full `error feedback` (Debug).
- **Atomic Write Strategy:** Replaced manual backup `.yml` files with an atomic write process in `manager.py` to ensure data integrity.
- **Utils Directory:** Centralized shared functions into a new `/utils` folder, nuking redundant `helper.py` functions.
- **Output Buffering:** Migrated `version.py` output from direct loops to a buffered string approach to minimize `print()` overhead.

### Changed
- **O(n) to O(1) Migration:** Refactored `system/syntax/dispatcher` to use dictionary/config-based lookups instead of iterative scanning.
- **Version Control Consolidation:** Merged `scanner.py` and `sync.py` into a single `version.py` since the read/write logic was 90% identical.
- **Parser Overhaul:** Complete rewrite of `system/syntax/parser.py` for better maintainability and logic flow. Commands are now stored in `config.yml`.
- **License Pivot:** Re-licensed the project from GPLv3 to Apache-2.0.

### Improved
- **Geometry Logic:** Refactored `submodulesA` (triangle/rectangle) to assume the largest value for hypotenuse/perimeter cases, while maintaining traditional detection for area.
- **Color Integration:** Added a color utility system for terminal output (Error, Info, Success, etc.).

### Fixed
- **Code Bloat:** Removed `system/settings/default.yml` and `backup.yml` as they are no longer needed with the new atomic write system.
- **Parameter Cleanup:** Deleted the "perimeter" argument in `triangle/engine.py` to avoid controversial/strict input results.

</details>

---

<details>
<summary><b>v0.2.0 beta 2026/04/09</b></summary>

### Added
- Added support for triangle calculations.
- Improved internal system for handling input and version syncing.
### Improved
- Overall system performance and consistency have been enhanced.
- Configuration system is now cleaner and more reliable.
### Fixed
- Fixed incorrect documentation link.
- Removed unnecessary internal processes to make the system more efficient.

</details>

---

<details>
<summary><b>v0.1.1 beta 2026/04/05</b></summary>

### Fixed
- fix argument parsing issue where second value was not detected
- fix inconsistent return values causing unexpected None outputs
### Changed
- minor refactor of argument handling logic
- improve argument parsing to handle multiple values correctly

</details>

---

<details>
<summary><b>v0.1.0 beta 2026/04/03</b></summary>

### Added
- initial release (beta)
- basic geometry modules (circle, square, rectangle) 
### Notes
- still in beta, may break sometimes

</details>

---

> [!NOTE]
> Confused about the **new features** or found a **bug**? Feel free to reach out! You can contact me through my **social media** for a quick chat. I’m more than happy to explain things further in [**Bahasa Indonesia**](https://en.wikipedia.org/wiki/Indonesian_language).
