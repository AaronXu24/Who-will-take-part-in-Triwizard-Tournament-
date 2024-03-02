import tkinter as tk
from PIL import ImageTk, Image 
import os
import random
import sys
import re
import time

name_list = []
drop_name_gif = r"./picture/dropname.gif"
get_name_gif = r"./picture/getname.gif"
# drop_name_gif = r"E:\Program\Python\Final project\picture\dropname.gif"
# get_name_gif = r"E:\Program\Python\Final project\picture\getname.gif"
gif_frames = []
loop = None
choice_order = 1


def main():
    drop_name_page()


def return_gif_frames(gif_name):
    """
    Returns a list of PhotoImage objects from a given GIF file.
    """
    img = Image.open(gif_name)
    frames = img.n_frames
    photoimage_objects = []
    for i in range(frames):
        obj = tk.PhotoImage(file=gif_name, format=f"gif -index {i}")
        photoimage_objects.append(obj)
    return photoimage_objects


def animation(gif_label, window, gif_name, current_frame=0):
    """
    Animates a given GIF file on a given label in a given window.
    """
    global gif_frames, loop
    image = gif_frames[current_frame]
    gif_label.configure(image=image)
    current_frame = (current_frame + 1) % len(gif_frames)
    loop = window.after(50, lambda: animation(gif_label, window, gif_name, current_frame))


def stop_animation(window):
    """
    Stops the animation loop in a given window.
    """
    global loop
    if loop is not None:
        window.after_cancel(loop)
        loop = None


def title_name(name):
    """
    Capitalizes the first letter of each word in a given name.
    """
    return re.sub(r"[A-Za-z]+('[A-Za-z]+)?",
                  lambda mo: mo.group(0).capitalize(),
                  name)


def get_entry_name(name_entry):
    """
    Retrieves the name from a given entry widget.
    """
    name = name_entry.get()
    name_entry.delete(0, tk.END)
    return name


def drop_name(name):
    """
    Adds a given name to the global name list.
    """
    name = title_name(name)
    if name not in name_list:
        name_list.append(name)

def name_remove(name):
    global name_list
    name_list.remove(name)


def get_name(choice_order, name_list):
    """
    Returns a random name from the global name list.
    If there are no names in the list, exits the program.
    """
    if choice_order <= 3:
        try:
            name = random.choice(name_list)
            return name
        except IndexError:
            print(name_list)
            sys.exit("Cannot choose from an empty name list") 
    elif choice_order == 4:
        return "Harry Potter"
        


def show_name(name_list, window):
    """
    Displays a random name from the global name list in a given window.
    """
    global choice_order
    color = ["#FF5151","#FFFF93", "#00FFFF","#800000"]
    name = get_name(choice_order,name_list)
    if name != "":
        lbl_order = tk.Label(window, text=return_times(choice_order)+" name is: ", fg="black", bg=color[choice_order-1])
        lbl_name = tk.Label(window, text=name, fg="black", bg="white")
        lbl_order.grid(row=choice_order, column=0, padx=5, pady=5, sticky="nw")
        lbl_name.grid(row=choice_order, column=1, padx=5, pady=5,sticky="nwe")       

    if choice_order <= 3:
        name_remove(name)
        
    if choice_order == 3:
        choice_order += 1 
        time.sleep(5)
        show_name(name_list, window) 

    choice_order += 1


def return_times(times):
    """
    Returns a string indicating the ordinal number of a given integer.
    """
    if times == 1:
        return "1st "
    elif times == 2:
        return "2nd "
    elif times == 3:
        return "3rd "
    elif times == 4:
        return "4th "    
    else:
        return ""


def close_window(window):
    """
    Closes a given window.
    """
    window.destory()


def drop_name_page():
    """
    Creates a window for dropping names into the Goblet of Fire.
    """
    global gif_frames
    global drop_page_w
    drop_page_w = tk.Tk()
    drop_page_w.title("Drop your name into the Goblet:")
    drop_page_w.rowconfigure(0, minsize=400, weight=1)
    drop_page_w.columnconfigure(0, minsize=300, weight=1)
    gif_lbl = tk.Label(drop_page_w, image="")
    gif_lbl.grid(row=4, column=0, sticky="nsew", padx=5, pady=5)
    frm_buttons = tk.Frame(drop_page_w, relief=tk.RAISED, bd=2)
    name_lbl = tk.Label(master=frm_buttons, text="Please write down your name:")
    name_lbl.grid(row=0, column=0, sticky="nw", padx=5, pady=5)
    name_ent = tk.Entry(master=frm_buttons)
    name_ent.grid(row=0, column=1, sticky="ne", padx=5, pady=5)
    drop_lbl = tk.Label(master=frm_buttons, text="Drop your name into the Goblet:")
    drop_lbl.grid(row=1, column=0, sticky="nw", padx=5, pady=5)
    drop_btn = tk.Button(frm_buttons, text="Drop", bg="blue", fg="yellow", command=lambda: 
                         [animation(gif_lbl, drop_page_w, drop_name_gif, current_frame=0), 
                          drop_name(get_entry_name(name_ent))])
    drop_btn.grid(row=1, column=1, sticky="", padx=5, pady=5)
    done_lbl = tk.Label(master=frm_buttons, text="Have all names been dropped into the Goblet?")
    done_lbl.grid(row=2, column=0, sticky="", padx=5, pady=5)
    yes_btn = tk.Button(frm_buttons, text="Yes", bg="Green", fg="yellow", 
                        command=creat_name_page)
    yes_btn.grid(row=3, column=0, sticky="", padx=5, pady=5)
    no_btn = tk.Button(frm_buttons, text="No", bg="red", fg="yellow", 
                       command=lambda: stop_animation(drop_page_w))
    no_btn.grid(row=3, column=1, sticky="", padx=5, pady=5)
    frm_buttons.grid(row=0, column=0, sticky="new")
    gif_frames = return_gif_frames(drop_name_gif)
    drop_page_w.mainloop()

def creat_name_page():
    """
    Creates a window for choosing names from the Goblet of Fire.
    """
    global gif_frames, loop, choice_order,drop_page_w
    drop_page_w.destroy()
    gif_frames = []
    loop = None
    choice_order = 1
    name_page = tk.Tk()
    name_page.title("Who will take part in Triwizard Tournament?")

    choose_gif = tk.Label(master=name_page, image="")
    choose_gif.grid(row=5, column=0, sticky="nsew",columnspan=2,padx=5, pady=5)
      
    name_page.rowconfigure(0, minsize=100, weight=1)
    name_page.columnconfigure(0, minsize=500, weight=1)
    btn_choose = tk.Button(
        master=name_page,
        text="Let's choose the name!",
        command=lambda: [animation(choose_gif, name_page, get_name_gif, current_frame=0), 
                         show_name(name_list, name_page)]
    )
    btn_choose.grid(row=0, column=0, sticky="new",columnspan=2, padx=5, pady=5)

    gif_frames = return_gif_frames(get_name_gif)
    name_page.mainloop()


if __name__ == "__main__":
    main()