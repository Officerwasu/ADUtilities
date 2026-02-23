#  README.md

# Username Variation Generator

A lightweight Python tool to generate common username formats used in AD, Linux, and corporate environments. Useful for enumeration during pentesting or automation.

---

##  Features

* Accepts **First Last** and **First.Last** formats
* Generates multiple username variations
* Supports custom input/output files
* Removes duplicates automatically

---

##  Usage

### Basic

```bash
python3 gen_user.py -i names.txt
```

### Specify output file

```bash
python3 gen_user.py -i names.txt -o users_final.txt
```

### Help

```bash
python3 gen_user.py -h
```

---

##  Input Examples

```
James Roberts
Sarah.Osvald
```

---

##  Output Examples

```
james.roberts
jroberts
jamesr
james_roberts
jr
```

---

##  Authors

PaiN05, Uday

---
