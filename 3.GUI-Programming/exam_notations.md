## Here some notes about the exam

- You can call, throw commands, a callback from a widget using the method `invoke()`.
- You can access all properties from a widget using:
    - Throw methods:
        - `wdg.cget("name_property")`
        - `wdg.config(name_property="hi")`
    - Throw direct access:
        - `wdg["name_property"] = "hi"`
        - `wdg["name_property"]`
- You can get the value saved into an entry widget using `get()`
- If you invoke the method resizable __without arguments__ i won't allow the user to resize the window
- From the HEX colors:
    - Has 6 digits.
    - All 0 means black.
    - All F means white.
- The color model used by tkinter is __additive__.
- `fg` stands for __foreground__ not __foregroundcolor__.


---

NOTES:

- Get notes about th observable variables
- States of a widget
- tkinter possible shapes
- own methods from all widgets
- bind events
