# How to & where to ask programming questions & doubts?
- **Online Forums:**(Here you can ask question with proper etiquettes)
    - [Stack Overflow](https://stackoverflow.com/)
    - [Reddit](https://www.reddit.com/r/learnprogramming/)
- **How to ask?**
    - Explain what you are trying to do, not just what you did. This lets your helper know if you are on the wrong track.
    - Specify the point at which the error happens. Does it occur at the very start of the program or only after you do a certain action?
    - When sharing error messages or code online (e.g., via email or forums), it's best to copy and paste the full code or error into a tool like Pastebin or GitHub Gist. These services preserve formatting and make sharing easier. After posting, simply share the generated URL. Examples include:
        - [Patebin](https://pastebin.com/SzP2DbFx/)
        - [Github Gist](https://gist.github.com/)
    - Explain what you’ve already tried to do to solve your problem. This
    tells people you’ve already put in some work to figure things out on
    your own.
    - List the version of Python you’re using. (There are some key
    differences between version 2 Python interpreters and version 3
    Python interpreters.) Also, say which operating system and version
    you’re running.
    -  If the error came up after you made a change to your code, explain
    exactly what you changed.
    - Say whether you’re able to reproduce the error every time you run
    the program or whether it happens only after you perform certain
    actions. If the latter, then explain what those actions are.

**Operator:** Operator in special symbol which perform specific task on operands.

|Operator|Operation|Example|Answer|
|---------|--------|-------|------|
|**       |Exponent|2**4    |16   |
|%        |Modulus |10%2    |0    |
|//       |floor division operator|7//2|3|
|/|Division|10/2|0|
|*|Multiplication|10*10|100|
|-|Subtraction|100-10|90|
|+|Addition|10+90|100|

## The Integer, Floating-Point, and String Data Types
1. Integer(int)
- Represents whole numbers (no decimal point).
- Can be positive, negative, or zero.
Examples:
```
x = 10
y = -25
z = 0
```
- Python automatically handles very large integers:<br>
`big = 12345678901234567890
`
2. Floating-Point(float)
- Represents real numbers (with decimal points).
- Can also be used for scientific notation.
Examples:
```
a = 3.14
b = -0.001
c = 2e3  # 2000.0 in scientific notation
```
3. String(str)
- Represents sequences of Unicode characters (text).
- Enclosed in single ' or double " quotes.
Examples:
```
name = "Sakshi"
greeting = 'Hello, Sakshi!'
multi_line = """Love is just attraction, I can't love you because I can't grow with you."""

# String concatenation and replication: **`+` operator is used to concate two strings. It won't change origina string instead create new one after concatenation**

```firstName="Hello"
lastName="World!"
newString=firstName+lastName
print("firstName: ",firstName)
print("lastName: ",lastName)
print("newString: ",newString)
```
