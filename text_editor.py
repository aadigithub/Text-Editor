import tkinter as tk
from tkinter import ttk
from tkinter import font,messagebox,colorchooser,filedialog
import os
main_application = tk.Tk()
main_application.geometry('1220x780')
main_application.title('My Text Editor')


# ------------------------  Main Menu ----------------------
main_menu = tk.Menu()


def action():
    pass
#file menu icons
new_icon = tk.PhotoImage(file = 'icons/new.png')
open_icon = tk.PhotoImage(file = 'icons/open.png')
save_icon = tk.PhotoImage(file = 'icons/save.png')
save_as_icon = tk.PhotoImage(file = 'icons/save_as.png')
exit_icon = tk.PhotoImage(file = 'icons/exit.png')

# file menubar
file_menu = tk.Menu(main_menu, tearoff = 0)
main_menu.add_cascade(label = 'File', menu = file_menu  )


# edit menu icons
# undo_icon = tk.PhotoImage(file = 'icons/undo.png')
# redo_icon = tk.PhotoImage(file = 'icons/redo.png')
cut_icon = tk.PhotoImage(file = 'icons/cut.png')
copy_icon = tk.PhotoImage(file = 'icons/copy.png')
paste_icon = tk.PhotoImage(file = 'icons/copy.png')
clear_all_icons=tk.PhotoImage(file='icons/clear_all.png')
find_icon = tk.PhotoImage(file = 'icons/find.png')

# edit menubar
edit_menu = tk.Menu(main_menu,tearoff = 0)
main_menu.add_cascade(label =" Edit" ,menu = edit_menu)


# view icons
toolbar_icon = tk.PhotoImage(file='icons/tool_bar.png')
statusbar_icon =tk.PhotoImage(file='icons/status_bar.png')

# view menubar
view_menu = tk.Menu(main_menu,tearoff = 0)
main_menu.add_cascade(label =" View" ,menu = view_menu)


# clour theme icons
light_default_icon =tk.PhotoImage(file='icons/light_default.png')
light_plus_icon =tk.PhotoImage(file='icons/light_plus.png')
night_blue_icon =tk.PhotoImage(file='icons/night_blue.png')
red_icon =tk.PhotoImage(file='icons/red.png')
monokai_icon =tk.PhotoImage(file='icons/monokai.png')
dark_icons = tk.PhotoImage(file='icons/dark.png')

color_theme_menu = tk.Menu(main_menu,tearoff = 0)

theme_choice =tk.StringVar()
color_icons =(light_default_icon, light_plus_icon, dark_icons, red_icon, monokai_icon, night_blue_icon)

color_dict ={
    'Light Default' : ('#000000','#ffffff'),
    'Light Plus' : ('#474747','#e0e0e0'),
    'Dark' : ('#c4c4c4','#2d2d2d'),
    'Red' : ('#2d2d2d','#ffe8e8'),
    'Monakai' : ('#b3b774','#474747'),
    'Night Blue' : ('#ededed','#6b9dc2')
}

# color theme
main_menu.add_cascade(label =" Color Theme" ,menu = color_theme_menu)

# ------------------------ End Main Menu -------------------

# ------------------------  Toolbar ----------------------
tool_bar =ttk.Label(main_application)
tool_bar.pack(side=tk.TOP,fill =tk.X)

# font box
font_tuple = tk.font.families()
font_family =tk.StringVar()
font_box =ttk.Combobox(tool_bar,width =30, height=10,textvariable=font_family,state='readonly')
font_box['values']= font_tuple
font_box.current(font_tuple.index('Arial'))
font_box.grid(row =0,column =0,padx= 5)

# font size
size_var =tk.IntVar()
font_size = ttk.Combobox(tool_bar,width =14,textvariable =size_var )
font_size['values'] =tuple(range(8,72,2))
font_size.current(4)
font_size.grid(row=0,column =1,padx=5)

# bold button
bold_button_icons =tk.PhotoImage(file='icons/bold.png')
bold_button = tk.Button(tool_bar,image=bold_button_icons)
bold_button.grid(row=0,column=2,padx=5)

# italic button
italic_button_icons =tk.PhotoImage(file='icons/italic.png')
italic_button = tk.Button(tool_bar,image=italic_button_icons)
italic_button.grid(row=0,column=3,padx=5)

# uderline button
underline_button_icons =tk.PhotoImage(file='icons/underline.png')
underline_button = tk.Button(tool_bar,image=underline_button_icons)
underline_button.grid(row=0,column=4,padx=5)

# font_color button
font_color_icon =tk.PhotoImage(file='icons/font_color.png')
font_color_button = tk.Button(tool_bar,image=font_color_icon)
font_color_button.grid(row=0,column=8,padx=5)

# align center
align_center_icons =tk.PhotoImage(file='icons/align_center.png')
align_center_button =tk.Button(tool_bar,image=align_center_icons)
align_center_button.grid(row=0,column=5,padx=5)

# align left
align_left_icons =tk.PhotoImage(file='icons/align_left.png')
align_left_button =tk.Button(tool_bar,image=align_left_icons)
align_left_button.grid(row=0,column=6,padx=5)

# align right
align_right_icons =tk.PhotoImage(file='icons/align_right.png')
align_right_button =tk.Button(tool_bar,image=align_right_icons)
align_right_button.grid(row=0,column= 7,padx=5)


# ------------------------ End Toolbar -------------------


# ------------------------  Text Editor ----------------------
text_editor =tk.Text(main_application)
text_editor.config(wrap='word',relief=tk.FLAT)

scroll_bar = tk.Scrollbar(main_application)
text_editor.focus_set()
scroll_bar.pack(side=tk.RIGHT,fill=tk.Y)
scroll_bar.config(command= text_editor.yview)
text_editor.pack(fill=tk.BOTH,expand=True)

text_editor.config(yscrollcommand=scroll_bar.set)

# font size and family
current_font_family ='Arial'
current_font_size =12

def change_font(main_application):
    global current_font_family
    current_font_family = font_family.get()
    text_editor.configure(font=(current_font_family,current_font_size))


def change_font_size(main_application):
    global current_font_size
    current_font_size =size_var.get()
    text_editor.configure(font=(current_font_family,current_font_size))


font_box.bind("<<ComboboxSelected>>",change_font)
font_size.bind("<<ComboboxSelected>>",change_font_size)


# Buttons functionality
# Bold button functinality

def change_bold():
    text_property = tk.font.Font(font=text_editor['font'])
    print(text_property)
    if text_property.actual()['weight'] == 'normal':
        text_editor.configure(font=(current_font_family,current_font_size,'bold'))
    if text_property.actual()['weight'] =='bold':
        text_editor.configure(font=(current_font_family,current_font_size,'normal'))

bold_button.configure(command= change_bold)

# Italic button functinality
def change_italic():
    text_property= tk.font.Font(font=text_editor['font'])
    if text_property.actual()['slant']=='roman':
        text_editor.configure(font=(current_font_family,current_font_size,'italic'))
    if text_property.actual()['slant']=='italic':
        text_editor.configure(font=(current_font_family,current_font_size,'roman'))

italic_button.configure(command =change_italic)

# Underline button functinality
def change_underline():
    text_property= tk.font.Font(font=text_editor['font'])
    if text_property.actual()['underline']== 0:
        text_editor.configure(font=(current_font_family,current_font_size,'underline'))
    if text_property.actual()['underline']== 1:
        text_editor.configure(font=(current_font_family,current_font_size,'normal'))

underline_button.configure(command =change_underline)

#fontcolor functionality
def change_font_colour():
    color_var=tk.colorchooser.askcolor()
    
    text_editor.configure(fg=color_var[1])

font_color_button.configure(command=change_font_colour)

# align functionality

def align_left():
    text_content =text_editor.get(1.0,'end')
    text_editor.tag_config('left',justify=tk.LEFT)
    text_editor.delete(1.0,tk.END)
    text_editor.insert(tk.INSERT,text_content,'left')

align_left_button.configure(command=align_left)

def align_right():
    text_content =text_editor.get(1.0,'end')
    text_editor.tag_config('right',justify=tk.RIGHT)
    text_editor.delete(1.0,tk.END)
    text_editor.insert(tk.INSERT,text_content,'right')

align_right_button.configure(command=align_right)

def align_center():
    text_content =text_editor.get(1.0,'end')
    text_editor.tag_config('center',justify=tk.CENTER)
    text_editor.delete(1.0,tk.END)
    text_editor.insert(tk.INSERT,text_content,'center')

align_center_button.configure(command=align_center)


text_editor.configure(font=('Arial',12))
# ------------------------ End Text Editor -------------------


# ------------------------  Status Bar ----------------------

status_bar= ttk.Label(main_application,text='Status')
status_bar.pack(side=tk.BOTTOM)

text_changed = False
def changed(main_application):
    if text_editor.edit_modified():
        global text_changed
        text_changed =True
        words =len(text_editor.get(1.0,'end-1c').split())
        characters= len(text_editor.get(1.0,'end-1c').replace(' ', ''))
        status_bar.config(text=f'Characters :{characters} Words : {words}')
    text_editor.edit_modified(False)

text_editor.bind('<<Modified>>',changed)
# ------------------------ End Status Bar -------------------

# ------------------------  Main Menu functionality ----------------------
#variable 
url= ''

# new file
def new_file(event=None):
    global url
    url =''
    text_editor.delete(1.0,tk.END)

file_menu.add_command(label = 'New', image=new_icon,compound =tk.LEFT,accelerator = 'Ctrl+N',command =new_file)
# open_file
def open_file(event = None):
    global url
    url = filedialog.askopenfilename(initialdir = os.getcwd(), title='Select File', filetypes=(('Text File','*.txt'),('All Files','*.*')))
    try:
        with open(url,'r') as fr:
            text_editor.delete(1.0,tk.END)
            text_editor.insert(1.0,fr.read())
    except FileNotFoundError:
        return
    except:
        return
    main_application.title(os.path.basename(url))
# file command
file_menu.add_command(label = 'Open', image=open_icon,compound =tk.LEFT,accelerator = 'Ctrl+O',command=open_file)

# save file
def save_file(event= None):
    global url
    try:
        if url:
            content = str(text_editor.get(1.0,tk.END))
            with open(url,'w',encoding= 'utf-8') as fw:
                fw.write(content)
        else:
             url = filedialog.asksaveasfile(mode = 'w', defaultextension='.txt', filetypes=(('Text File','*.txt'),('All Files','*.*')))        
             content2 = text_editor.get(1.0,tk.END)
             url.write(content2)
             url.close()
    except:
            return   
# save command
file_menu.add_command(label = 'Save',image=save_icon, command = save_file,compound =tk.LEFT,accelerator = 'Ctrl+S')

# save as functinality

def save_as(event= None):
    global url
    try:
        content = text_editor.get(1.0,tk.END)
        url = filedialog.asksaveasfile(mode = 'w', defaultextension='.txt', filetypes=(('Text File','*.txt'),('All Files','*.*'))) 
        url.write(content)
        url.close()
    except:
        return
# save_as command 
file_menu.add_command(label = 'Save as', image=save_as_icon,command = save_as,compound =tk.LEFT,accelerator = 'Ctrl+Alt+S')

# file  commands
# exit functinality
def exit_text_editor(event=None):
    global url,text_changed
    try:
        if text_changed:
            mbox =messagebox.askyesnocancel("warning","Do you want to save the file ?")
            if mbox is True:
                if url:
                    content = text_editor.get(1.0,tk.END)
                    with open(url,'w',encoding='utf-8') as fw:
                        fw.write(content)
                        main_application.destroy()
                else:
                    content2= str(text_editor.get(1.0,tk.END))
                    url = filedialog.asksaveasfile(mode = 'w', defaultextension='.txt', filetypes=(('Text File','*.txt'),('All Files','*.*')))
                    url.write(content2)
                    url.close()
                    main_application.destroy()
            elif mbox is False:
                main_application.destroy()
                
            else:
                main_application.destroy()
    except:
        return


# exit command

file_menu.add_separator()
file_menu.add_command(label = 'Exit', image=exit_icon,command = exit_text_editor,compound =tk.LEFT,accelerator = 'Ctrl+Q')

# edit menu commands
# edit_menu.add_command(label = 'Undo', command = action,image=undo_icon,compound =tk.LEFT,accelerator = 'Ctrl+Z')
# edit_menu.add_command(label = 'Redo', command = action,image=redo_icon,compound =tk.LEFT,accelerator = 'Ctrl+Y')
# edit_menu.add_separator()
edit_menu.add_command(label = 'Cut',image=cut_icon,compound =tk.LEFT,accelerator = 'Ctrl+C',command=lambda:text_editor.event_generate("<Control c>"))
edit_menu.add_command(label = 'Copy', command = lambda:text_editor.event_generate("<Control x>"),image=copy_icon,compound =tk.LEFT,accelerator = 'Ctrl+X')
edit_menu.add_command(label = 'Paste', command = lambda:text_editor.event_generate("<Control v>"),image=paste_icon,compound =tk.LEFT,accelerator = 'Ctrl+V')
edit_menu.add_command(label = 'Clear All', command = lambda:text_editor.delete(1.0,tk.END),image=clear_all_icons,compound =tk.LEFT,accelerator = 'Ctrl+Alt+X')
edit_menu.add_separator()

# find functinality
def find(event =None):
    
    def find_text():
        word =find_label_entry.get()
        text_editor.tag_remove('match','1.0' ,tk.END)
        matches =0
        if word:
            start_pos ='1.0'
            while True:
                start_pos = text_editor.search(word,start_pos,stopindex=tk.END)
                if not start_pos:
                    break
                end_pos= f'{start_pos}+{len(word)}c'
                text_editor.tag_add('match',start_pos, end_pos)
                matches += 1
                start_pos =end_pos
                text_editor.tag_config('match',foreground='white',background='blue')


    def replace_with():
        word =find_label_entry.get()
        replace_text =replace_label_entry.get()
        content =text_editor.get(1.0,tk.END)
        new_content=content.replace(word,replace_text)
        text_editor.delete(1.0,tk.END)
        text_editor.insert(1.0,new_content)



    find_dialog =tk.Toplevel()
    find_dialog.geometry('350x150+400+200')
    find_dialog.title('Find')
    find_dialog.resizable(0,0)

    ## frame 
    find_frame = ttk.LabelFrame(find_dialog,text="Find/Replace",)
    find_frame.pack(pady=20)
     
    ## labels
    find_label =ttk.Label(find_frame,text='Find :')
    find_label.grid(row=0,column=0,padx=4,pady=4)
    replace_label =ttk.Label(find_frame,text='Replace :')
    replace_label.grid(row=1,column=0,padx=4,pady=4)
    
    
    ## Label entry box
    find_label_entry =ttk.Entry(find_frame,width=30)
    find_label_entry.grid(row=0,column=1,padx=4,pady=4)
    replace_label_entry =ttk.Entry(find_frame,width=30)
    replace_label_entry.grid(row=1,column=1,padx=4,pady=4)

    ## buttons
    find_button =ttk.Button(find_frame,text='Find',command= find_text)
    find_button.grid(row=2,column=0,padx=4)
    replace_button =ttk.Button(find_frame,text='Replace',command=replace_with)
    replace_button.grid(row=2,column=1,padx=4)
    
edit_menu.add_command(label  = 'Find',image=find_icon,compound =tk.LEFT,accelerator = 'Ctrl+F',command=find)

# views checkbuttons command

show_toolbar =tk.BooleanVar()
show_toolbar.set(True)
show_statusbar =tk.BooleanVar()
show_toolbar.set(True)

def hide_toolbar():
    global show_toolbar
    if show_toolbar:
        tool_bar.pack_forget()
        show_toolbar =False
    else:
        text_editor.pack_forget()
        status_bar.pack_forget()
        tool_bar.pack(side=tk.TOP,fill=tk.X)
        text_editor.pack(fill=tk.BOTH,expand=True)
        status_bar.pack(side =tk.BOTTOM)
        show_toolbar=True

def hide_statusbar():
    global show_statusbar
    if show_statusbar:
        status_bar.pack_forget()
        show_statusbar =False
    else:
        status_bar.pack(side= tk.BOTTOM,fill=tk.X)
        show_statusbar =True
        

view_menu.add_checkbutton(label = 'Tool Bar', command = hide_toolbar,image=toolbar_icon,compound= tk.LEFT,variable=show_toolbar)
view_menu.add_checkbutton(label = 'Status Bar', command = hide_statusbar,image=statusbar_icon, compound =tk.LEFT,variable=show_statusbar)

#color theme
def change_theme():
    choice_theme =theme_choice.get()
    color_tuple =color_dict.get(choice_theme)
    fg_color,bg_color = color_tuple[0],color_tuple[1]
    text_editor.config(background =bg_color, fg=fg_color)

count =0
for i in color_dict:
    color_theme_menu.add_radiobutton(label=i,image=color_icons[count],variable=theme_choice,compound=tk.LEFT)
    count = count + 1
# ------------------------ End Main Menu Functionality-------------------

### --------------- Bind Shortcut keys -------------------
main_application.bind("<Control-n>",new_file)
main_application.bind("<Control-o>",open_file)
main_application.bind("<Control-s>",save_file)
main_application.bind("<Control-Alt-s>",save_as)
main_application.bind("<Control-q>",exit_text_editor)
main_application.bind("<Control-f>",find)


main_application.config(menu = main_menu)
main_application.mainloop()


