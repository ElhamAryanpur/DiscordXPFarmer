# Discord XP Farmer Bot

> NOTE: I am not responsible for anything! In any case you use this tool, you
> are liable for it!

## About

This is a bot for `farming XP` of `MEE6` bot on `discord` to get higher ranks faster.
As MEE6 give randomly `from 15 to 25` points `each minute`, by default this bot is
set to talk at that rate as well.

All this bot does is to take `control` of your `mouse` and `keyboard` and write a
`random` thing from it's [Database](misc/db.py) which can be updated as well.

## Usage

This is `python 3` based module and it can be imported and used by code. let's do
`step by step` shall we?

### Step 1 Download Requirements

Two things are required:

1. `Python Programming language`: Which can be downloaded from
   [Here](https://www.python.org)

2. `Pynput Module`: which can be downloaded either by doing "`python -m pip
   install pynput`" on commandline or let the script download it for you.

After those two are ready, we can start using the bot:

```bash
git clone https://www.github.com/ElhamAryanpur/DiscordXPFarmer
```

### Step 2 import

you can import the bot like:

```python
import DXPF
```

and initialize it:

```python
bot = DXPF.DXPF()
```

### Step 3 adjust settings

There are `3` settings avaliable to adjust:

1. `.speed`: `int`; default: `0.3`. defines amount of delay between each keypress when typing
   messages. can be set by seconds.

2. `.delay`: `int`; default: `60`. defines amount of delay between each messages
   to be sent

3. `.mousePosition`: `tuple`; default: `(500,500)`. defines position of mouse in
   the screen as x and y. This position will be used to click and type the
   message.

an example adjustment can look like:

```python
bot.speed = 0.2
```

To get current position of mouse:

```python
bot.getCurrentPosition()
```

which will print current mouse position on the screen. if you want to save it
for bot usage, you can pass parameter `savePos=True`.

### Step 4 Run

To run the bot, all you have to do is:

```python
bot.startWriting()
```

it also takes a parameter `mousePos=(x,y)` to set position of mouse.

After running that function, the bot will send `random message` from `DB`, at a
specific `key press rate`, with specific `delay` between each message.

Increase size of `DB` or make words you say mostly to trick others that it is
you rather than bot.

## Conclusion

That was all for now... more features coming soon...

If you had problems, you can open an issue. or contact me by
[Facebook](https://www.facebook.com/elham.aryanpur.10),
[Instagram](https://www.instagram.com/elham_aryanpur), or discord with tag
`#9162`.

> Enjoy!
