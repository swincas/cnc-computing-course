---
marp: true
theme: cn5_style
footer: slides by Lukas Steinwender
---

<!-- _class: titleslide -->
# Command
## Intro to Bash

![bg](../../gfx/TitlePage.png)
<div class="footnote">Image generated with ChatGPT</div>

---

# Bash (Bourne Again SHell)
* command interpreter for Unix-like operating systems
* everything interpreted as string on basic level
* case sensitive
* metacharacters: `\n`, `\ `, `\t`, `|`, `&`, `;`, `(`, `)`, `<`, `>`

> used by many high-performance clusters (HPC) around the globe

--- 
# Startup Files and `.bashrc`
* startup files
    * `/etc/profile`
    * `~/.bash_profile`
    * `~/.bash_login`
    * `~/.profile`
    * `~/.bash_logout`
    * `~/.bashrc`
* called whenever a new session is launched
* can call other scripts from within them

---
# Bash Scripts
* follow this structure 
```bash
#!/bin/env bash
<your code>
```
* `#!/bin/env bash` ... shebang

# Useful Commands
$$\textcolor{red}{\text{TODO: continue}}$$