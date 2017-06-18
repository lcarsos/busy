Busy
====

A terminal todo application for people serious about todo lists

---

Busy understands that you have a lot of things on your plate. It knows that your todo list is days long, and a hairy complicated mess. It understands that you can't work on some tasks until others are complete. It knows that sometimes you write down something in your list optimistically thinking that's all that you need to do, but when you sit down to work on it the complexity spirals out of control and you find many things that you need to do as part of that one task. Busy understands that working on one thing can forward the progress on several larger tasks. Busy knows that you aren't doing just one thing at a time.

And if you use Busy enough, since you've stored what you were busy doing and for how long, it can help you bill clients for time spent accurately.

Busy can help you:

- Remember the things you need to get done days, months, quarters out
- Organize what you did after you did it
- Find where to start
- Find something to fit into some unscheduled time

## Busy commands
To be as useful as possible, and as out of your way as possible, busy is primarily a CLI. So you can begin and stop work, switch tasks at the same prompt where you are doing your work.

### Doing work
- `busy` - quickly begin logging time to an unnamed task that you can organize later
- `busy with "this one thing"` - start working on a task with the name you provided. Creates a task if one doesn't unambiguously match.
- `busy stop` - Stop working on the current task (asks you which of the things you're busy with you're stopping)
- `busy switchto "fixing prod"` - stop working on what you were, and start a new task (for when emergencies pop up)
- `busy complete` - Call this task done (pass a name in if you're working on many things, or referencing some other task)

### Finding work
- `busy work [30m]` - Show a list of tasks that can be done
- `busy recent [1w]` - Show a list of tasks that have been worked on recently

## Other UIs
For the most part busy, is just an engine that keeps track of your todo list. Busy comes with a CLI, and an ncurses UI. It's possible to write other frontends for Busy (I don't know what the interface looks like for that yet).

- `busy -i`

