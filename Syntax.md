# Syntax Documentation

[Back](./README.md)

> it's still specific for shapes, might changes later

## General Use
### Command Format
All commands follow this positional hierarchy:

`$ <module> <argument> <val1> [val2] [val3]`

### Logic Rules
The system processes values based on the number of inputs and argument type:

1. **Single Input Modules (Circle, Square)**
   - Only requires `val1`.
   - The value is directly assigned to the property defined by the argument.

2. **Multi-Input Modules (Rectangle, Triangle)**
   - **Flexible Arguments (Basic)**: Used for base/sides (e.g., "b"). The system automatically sorts the values (e.g., largest becomes length/base).
   - **Strict Arguments (Specific)**: Used for specific properties (e.g., "d", "p", "a", "h"). `val1` is **always** treated as the property defined by the argument, regardless of its size.

---

<details>
<summary><b>Circle Syntax</b></summary>

`circle <argument> <val1>`

**Arguments**
- "r" → radius
- "d" → diameter
- "c" → circumference
- "a" → area

**Example**

```
$ circle r 7
Output
Radius        : 7cm
Diameter      : 14cm
Circumference : 43.98cm
Area          : 153.94cm²
```

</details>

---

<details>
<summary><b>Square Syntax</b></summary>

`square <argument> <val1>`

**Arguments**
- "s" → side
- "d" → diagonal
- "p" → perimeter
- "a" → area

**Example**

```
$ square s 6
Output
Side      : 6cm
Diagonal  : 8.49cm
Perimeter : 24cm
Area      : 36cm²
```

</details>

---

<details>
<summary><b>Rectangle Syntax</b></summary>

`rectangle <argument> <val1> <val2>`

**Arguments**
- "b" → base (Flexible: val1 & val2 are sorted into length & width)
- "d" → diagonal (Strict: val1 = diagonal, val2 = length/width)
- "p" → perimeter (Strict: val1 = perimeter, val2 = length/width)
- "a" → area (Strict: val1 = area, val2 = length/width)

**Behavior Rules**
- For argument **"b"**, the system automatically determines length (larger) and width (smaller).
- For arguments **"d", "p", "a"**, `val1` is strictly processed as the primary property.

**Example**

```
$ rectangle b 8 15
Output
Length    : 15cm
Width     : 8cm
Diagonal  : 17cm
Perimeter : 46cm
Area      : 120cm²
```

</details>

---

<details>
<summary><b>Triangle Syntax</b></summary>

`triangle <argument> <val1> <val2> [val3]`

**Arguments**
- "b" → base (Flexible: val1 & val2 are sorted into base & height)
- "h" → hypotenuse (Strict: val1 = hypotenuse, val2 = base/height)
- "p" → perimeter (Strict: val1 = perimeter, val2 & val3 = known sides)
- "a" → area (Strict: val1 = area, val2 = base/height)

**Behavior Rules**
- **Argument "b"**: Flexible sorting (Largest = Base, Smallest = Height).
- **Argument "h"**: Strict. `val1` is the Hypotenuse.
- **Argument "p"**: Strict. `val1` is the Perimeter. System calculates the 3rd side, then sorts all: Largest = Hypotenuse, Median = Base, Smallest = Height.
- **Argument "a"**: Strict. `val1` is the Area.

**Example**

```
$ triangle b 3 4
Output
Base       : 4cm
Height     : 3cm
Hypotenuse : 5cm
Perimeter  : 12cm
Area       : 6cm²
```

</details>

---

**Notes**
- This project is syntax-based and runs in a CLI environment.
- **Beta Notice**: Strict positional logic applies to multi-input specific arguments.
- Invalid input always return no output (None).
- This project is currently in beta.