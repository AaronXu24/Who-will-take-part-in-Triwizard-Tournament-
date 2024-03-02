# Who will take part in Triwizard Tournament?

#### Video Demo:  <URL HERE>

#### Description:

This project is just mimic the process of choosing the person to take part in the **Triwizard Tournament** (Which is a famous game in wizards' world). The process has two process:

- **Drop your name into the Goblet**:
  If you want to take part in the competition, you need to drop your name into the Goblet. In some way, if you do not drop your name, the Goblet will never choose you. But there are always accidents. We will see what will happen.

- **Wait the Goblet to choose the people**:
  If we have confirmed that all people who want to join this game have put their names into the Goblet, we can let the Goblet to choose the name. There will always be three people to be choosen. However, something unusual will happened.

#### Page display

- **Drop_name_page**:

You can write down your name in the box and drop the name into the Goblet by click the `Drop` button. Three or more names need to be droped into the Goblet. If you ensure names of these students who wanted join this game have been dropped into, then click the `yes` button.

![](https://u.cubeupload.com/AaronXu/dropnamepage.png)

- **Get_name_page**:
This page is quite simple. All you need is click the `Let's choose the name!` button three times and choose three people to take part in this game.

![](https://u.cubeupload.com/AaronXu/Getnamepage.png)


#### Files and Functions's Description

- project.py

  - `main()`: Run the drop_name_page()

  - `return_gif_frames(gif_name)`:Returns a list of PhotoImage objects from a given GIF file.

  - `animation(gif_label, window, gif_name, current_frame=0)`:Animates a given GIF file on a given label in a given window.

  - `stop_animation(window)`: Stops the animation loop in a given window.

  - `title_name(name)`: Capitalizes the first letter of each word in a given name.

  - `get_entry_name(name_entry)`: Retrieves the name from a given entry widget.

  - `drop_name(name)`:Adds a given name to the global name list.

  - `name_remove(name)`: Remove the name from the list

  - `get_name(choice_order, name_list)`:
    - Returns a random name from the global name_list.
    - If there are no names in the list, exits the program.

  - `show_name(name_list, window)`: Displays a random name from the global name list in a given window.

  - `return_times(times)`: Returns a string indicating the ordinal number of a given integer.

  - `close_window(window)`: Closes a given window.

  - `drop_name_page()`: Creates a window for dropping names into the Goblet of Fire.

  - `creat_name_page()`:Creates a window for choosing names from the Goblet of Fire.

