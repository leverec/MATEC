# Syntax Documentation

[Back to Home](./README.md)

> **Status:** MATEC is currently in Beta. Syntax is focused on mathematical logic and CLI system management.

## General Use
### Input Processing
MATEC categorizes inputs into two distinct types:

1. **Structured Commands (Geometry & System)**
   Follows a positional hierarchy:
   `$ <module> <argument> <val1> [val2] [val...]`
   - **Positional Logic**: The system interprets values based on their position relative to the argument.
   - **Argument-Driven**: The argument defines how the following values are assigned.

2. **Expression Parsing (Arithmetic Engine)**
   Follows standard mathematical notation:
   `$ <expression>`
   - **Direct Evaluation**: The system detects mathematical operators or constants and triggers the Arithmetic Engine automatically.

## Input Logic & Sorting Rules
To prevent illogical geometric calculations (e.g., a side longer than the hypotenuse), MATEC applies specific sorting rules based on the chosen argument:

### 1. Auto-Sorted Inputs
For these arguments, the system automatically reorders `<val1>` and `[val2]` to ensure mathematical consistency.
- **Triangle**: `b` (base), `h` (hypotenuse).
- **Rectangle**: `b` (base), `d` (diagonal), `p` (perimeter).
*Logic: The system determines which value represents the primary property based on magnitude to avoid calculation errors.*

### 2. Strict/Unsorted Inputs
For these arguments, `<val1>` is strictly assigned as the defined property and is never reordered.
- **Triangle**: `a` (area).
- **Rectangle**: `a` (area).
*Logic: The first value is always treated as the specific target value (e.g., the total Area).*

## System Commands

| Command | Action |
| :--- | :--- |
| `clear` / `cls` | Clear the terminal screen. |
| `exit` / `q` | Close the MATEC session. |
| `settings show` | Display all current configurations. |
| `settings get <key>` | Get value of a specific setting. |
| `settings set <key> <val>` | Update a setting (e.g., `precision`). |
| `debug version [path] [ver]` | Scan and read versioning across all Python files. |
| `debug version --sync` | Synchronize x.y versioning to match the project x.y.z format. |

## Submodules A (Geometry)

<details>
<summary><b>Circle Syntax</b></summary>

`circle <arg> <val1>`
- **Args**: `r` (radius), `d` (diameter), `c` (circumference), `a` (area).

</details>

<details>
<summary><b>Square Syntax</b></summary>

`square <arg> <val1>`
- **Args**: `s` (side), `d` (diagonal), `p` (perimeter), `a` (area).

</details>

<details>
<summary><b>Rectangle Syntax</b></summary>

`rectangle <arg> <val1> <val2>`
- **Args**: `b` (sorted), `d` (sorted), `p` (sorted), `a` (strict).

</details>

<details>
<summary><b>Triangle Syntax</b></summary>

`triangle <arg> <val1> <val2>`
- **Args**: `b` (sorted), `h` (sorted), `a` (strict).

</details>

## Submodules B (Arithmetic Engine)

### Functions & Roots
| Function | Syntax | Description |
| :--- | :--- | :--- |
| **Max/Min** | `max(<v1>, <v2>, ...)` | Find maximum or minimum values. |
| **Square Root** | `sqrt(<v1>)` / `√<v1>` | Calculate the square root of a value. |
| **Cube Root** | `cbrt(<v1>)` | Calculate the cube root of a value. |
| **Custom Root** | `root(<val>, [root_val])` | Calculates root of <val>. Defaults to square root (2) if [root_val] is empty. |
| **Power** | `power(<val>, <exp>)` | Calculates <val> to the power of <exp>. |

### Constants & Operators
- **Constants**: `pi`, `π`, `e`
- **Operators**: `+`, `-`, `*`, `x`, `×`, `/`, `:`, `÷`, `**`, `^`, `%`

**Example Usage:**
```text
$ 21 + 72 : 2 ^ √36 + (76 - 22) * (86 - -19) ÷ π × e
```

---

> [!NOTE]
> **AI-Assisted Documentation:** This documentation was generated and refined by **AI** to ensure linguistic precision and clarity, as the **author's primary language is not English.**
> 
> **Error Handling:** Any input that violates the defined syntax or positional logic will return a `None` value. Use **Debug Mode** for detailed feedback.
