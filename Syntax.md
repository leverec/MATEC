Syntax Documentation

General Usage

All commands follow this format:

`<shape> <argument> <value> [value]`

- Input is written in terminal style:

`$ <command>`

---

Circle

`circle <argument> <value>`

Arguments

- "r" → radius
- "d" → diameter
- "c" → circumference
- "a" → area

Example

```
$ circle r 7

Output

Radius        : 7cm
Diameter      : 14cm
Circumference : 43.98cm
Area          : 153.94cm²
```

---

```
Square

square <argument> <value>

Arguments

- "s" → side
- "d" → diagonal
- "p" → perimeter
- "a" → area

Example

$ square s 6

Output

Side      : 6cm
Diagonal  : 8.49cm
Perimeter : 24cm
Area      : 36cm²
```

---

```
Rectangle

rectangle <argument> <value> <value>

Arguments

- "b" → base (length & width input)
- "d" → diagonal + base
- "p" → perimeter + base
- "a" → area + base


Notes

- The system automatically determines:
  - length = larger value
  - width = smaller value

Example

$ rectangle b 8 15

Output

Length    : 15cm
Width     : 8cm
Diagonal  : 17cm
Perimeter : 46cm
Area      : 120cm²
```

---

Notes

- This project is syntax-based and runs in a CLI environment.
- Invalid input may return no output (None).
- This project is currently in beta.