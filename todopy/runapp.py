import curses


def header(stdscr):
    _, w = stdscr.getmaxyx()
    dashline = "=" * w
    intro = "Welcome to Todopy - Your terminal todo list"
    x, y = w // 2 - len(intro) // 2, 1
    stdscr.addstr(0, 0, dashline)
    stdscr.addstr(y, x, intro)
    stdscr.addstr(2, 0, dashline)


def todoHeader(stdscr):
    _, w = stdscr.getmaxyx()
    dashline = "=" * w
    intro = "Your daily tasks"
    x, y = w // 2 - len(intro) // 2, 4
    stdscr.addstr(3, 0, dashline)
    stdscr.addstr(y, x, intro)
    stdscr.addstr(5, 0, dashline)


def completedHeader(stdscr, len_tasks):
    _, w = stdscr.getmaxyx()
    dashline = "=" * w
    intro = "Your completed tasks"
    x, y = w // 2 - len(intro) // 2, 7 + len_tasks
    stdscr.addstr(y, 0, dashline)
    stdscr.addstr(y+1, x, intro)
    stdscr.addstr(y+2, 0, dashline)
   

def insertTask(stdscr, tasks):
    curses.echo()
    curses.curs_set(1)
    task = stdscr.getstr(6+len(tasks), 4)
    tasks.append(task)          
    curses.curs_set(0)
    curses.noecho()
    return tasks


def delTask(tasks, key):
    tasks.pop(key)
    return tasks
    

def swapPriority(tasks, key, second_key):
    tasks[key], tasks[second_key] = tasks[second_key], tasks[key]
    return tasks


def checkTask(tasks, completed, key):
    completed.append(tasks.pop(key))
    return tasks, completed


def main(stdscr):
    curses.curs_set(0)
    tasks, completed = [], []
    while True:
        stdscr.clear()
        header(stdscr)
        todoHeader(stdscr)
        completedHeader(stdscr, len(tasks))
        for idx, task in enumerate(tasks):
            stdscr.addstr(6+idx, 4, str(idx) + ': ' + str(task))
        for idx, check in enumerate(completed):
            stdscr.addstr(10+len(tasks)+idx, 4, str(idx) + ': ' + str(check))
        stdscr.refresh()
        key = stdscr.getch()
        if key == ord('i'):
            tasks = insertTask(stdscr, tasks)
        if key >= ord('0') and key < ord(str(len(tasks))):
            action_key = stdscr.getch()
            if action_key == ord('c'):
                tasks, completed = checkTask(tasks, completed, int(chr(key)))
            if action_key == ord('d'):
                tasks = delTask(tasks, int(chr(key)))
            if action_key == ord('s'):
                second_key = stdscr.getch()
                if second_key >= ord('0') and second_key < ord(str(len(tasks))):
                    tasks = swapPriority(tasks, int(chr(key)), int(chr(second_key)))
        if key == ord('q'):
            break        
    

curses.wrapper(main)
